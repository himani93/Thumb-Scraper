import cgi
import requests

from lxml import etree

from thumb_scraper.config import Config
from thumb_scraper.exceptions import *
from thumb_scraper.webpage import WebPage


class ThumbScraper(object):

    def __init__(self, url, pages, starting_page="0"):
        if not url:
            raise InvalidURLException("{} is not a valid URL".format(url))

        if type(pages) is not dict:
            raise InvalidPageException("Pages is not of type dict")

        self._base_url = url
        self._pages_to_scrape = pages
        self._starting_page = starting_page

    def _get_absolute_url(self, url=""):
        absolute_url = self._base_url

        if url:
            if self._base_url.endswith("/") and not url.startswith("/"):
                absolute_url = "{}{}".format(self._base_url, url)
            elif self._base_url.endswith("/") and url.startswith("/"):
                absolute_url = "{}{}".format(self._base_url, url[1:])
            elif not self._base_url.endswith("/") and url.startswith("/"):
                absolute_url = "{}{}".format(self._base_url, url)
            elif not self._base_url.endswith("/") and not url.startswith("/"):
                absolute_url = "{}/{}".format(self._base_url, url)

        return absolute_url

    def _get_webpage(self, url=""):
        absolute_url = self._get_absolute_url(url)

        try:
            response = requests.get(url=absolute_url, auth=(Config.USERNAME, Config.PASSWORD))
        except Exception as e:
            raise WebPageNotRetrievedException("{} not retrieved, Error: {}".format(url, e))

        if not response.ok:
            raise WebPageNotRetrievedException("{} not retrieved, status_code: {}".format(url, response.status_code))

        content_type, charset = cgi.parse_header(response.headers["Content-Type"])
        webpage = WebPage(url, response.content, content_type)

        return webpage

    def _scrape_page(self, page_name, url=""):
        if page_name not in self._pages_to_scrape:
            raise PageNotFoundException("{} page is not found in pages to scrape".format(page_name))

        page = self._pages_to_scrape[page_name]
        webpage = self._get_webpage(url)
        query = page.get("xpath_test_query")
        result = page.get("xpath_test_result")
        if webpage.is_tampered(query, result):
            raise PageTamperedException("Page {} is tampered".format(page_name))

        next_page_name = page["next_page_expected"]
        next_page_xpath_query = page["xpath_button_to_click"]
        next_page_url = webpage.evaluate_query(next_page_xpath_query)

        return next_page_name, next_page_url

    def scrape(self):
        page_name = self._starting_page
        page_url = ""
        pages_scraped = 0

        while True:
            try:
                page_name, page_url = self._scrape_page(page_name, page_url)
            except PageTamperedException as e:
                print "ALERT - can't move to page {}: page {} link has been malevolently tampered withh!".format(pages_scraped + 1, pages_scraped)
            else:
                pages_scraped += 1
                print "Moved to page {}".format(pages_scraped)