import pytest

from thumb_scraper.config import Config
from thumb_scraper.exceptions import *
from thumb_scraper.webpage import WebPage
from thumb_scraper.thumb_scraper import ThumbScraper


class TestThumbScraper(object):

    def test_thumb_scraper_creation(self):
        url = "https://yolaw-tokeep-hiring-env.herkoapp.com/"
        scraper = ThumbScraper(url=url, pages={})
        assert isinstance(scraper, ThumbScraper)
        assert scraper._base_url == url
        assert scraper._pages_to_scrape == {}
        assert scraper._starting_page == "0"

        with pytest.raises(InvalidURLException):
            ThumbScraper(url="", pages="")

        with pytest.raises(InvalidPageException):
            ThumbScraper(url=url, pages="")

    def test_get_web_page(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        scraper = ThumbScraper(url=url, pages={})
        webpage = scraper._get_webpage()
        assert isinstance(webpage, WebPage)

    def test_scrape_page(self):
        pass
