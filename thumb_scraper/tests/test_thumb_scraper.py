import pytest

from thumb_scraper.exceptions import *
from thumb_scraper.webpage import WebPage
from thumb_scraper.scraper import ThumbScraper


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

    def test_get_absolute_url(self):
        pass

    def test_get_web_page(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        scraper = ThumbScraper(url=url, pages={})
        webpage = scraper._get_webpage()
        assert isinstance(webpage, WebPage)
        assert webpage._url == url

    def test_scrape_page_when_page_not_found(self):
        page_name = "0"
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        pages = {}
        scraper = ThumbScraper(url, pages)

        with pytest.raises(PageNotFoundException):
            scraper._scrape_page(page_name, url)

    def test_scrape_page(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        pages = { "0":
                  {
                      "next_page_expected": "ada91079",
                      "xpath_button_to_click": "/html/body/div[2]/nav/div/div/ul/li[1]/div/div/div[3]/ul[2]/li[4]/a",
                      "xpath_test_query": "//*[@id=\"body\"]/div/div/section[1]/div/h2//text()",
                      "xpath_test_result": [
                          "\n    \n      Legalstart, le partenaire juridique de plus de 50 000 entrepreneurs\n    "]
                  }
        }
        scraper = ThumbScraper(url, pages)

        next_page_name, next_page_url = scraper._scrape_page("0")
        assert next_page_name == "ada91079"
        assert next_page_url == []

    def test_scrape_page_is_tampered(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        pages = { "0":
                  {
                      "next_page_expected": "ada91079",
                      "xpath_button_to_click": "/html/body/div[2]/nav/div/div/ul/li[1]/div/div/div[3]/ul[2]/li[4]/a",
                      "xpath_test_query": "//*[@id=\"body\"]/div/div/section[1]/div/h2//text()",
                      "xpath_test_result": ["Tampered Page"],
                  }
        }
        scraper = ThumbScraper(url, pages)
        with pytest.raises(PageTamperedException):
            next_page_name, next_page_url = scraper._scrape_page("0")

    def test_scrape_when_page_tampered(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        pages = { "0":
                  {
                      "next_page_expected": "ada91079",
                      "xpath_button_to_click": "/html/body/div[2]/nav/div/div/ul/li[1]/div/div/div[3]/ul[2]/li[4]/a",
                      "xpath_test_query": "//*[@id=\"body\"]/div/div/section[1]/div/h2//text()",
                      "xpath_test_result": ["Tampered Page"],
                  }
        }
        scraper = ThumbScraper(url, pages)
        scraped_result  = scraper.scrape()
        assert scraped_result == ["ALERT - can't move to page 1: page 0 link has been malevolently tampered withh!"]

    def test_scrape_when_next_page_is_unavailable(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        pages = { "0":
                  {
                      "next_page_expected": "ada91079",
                      "xpath_button_to_click": "/html/body/div[2]/nav/div/div/ul/li[1]/div/div/div[3]/ul[2]/li[4]/a",
                      "xpath_test_query": "//*[@id=\"body\"]/div/div/section[1]/div/h2//text()",
                      "xpath_test_result": ["\n    \n      Legalstart, le partenaire juridique de plus de 50 000 entrepreneurs\n    "],
                  }
        }
        scraper = ThumbScraper(url, pages)
        scraped_result  = scraper.scrape()
        assert scraped_result == ['Moved to page 1']

    def test_scrape_when_next_page_is_available(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com/"
        pages = {
            "0":
                  {
                      "next_page_expected": "ada91079",
                      "xpath_button_to_click": "/html/body/div[2]/nav/div/div/ul/li[1]/div/div/div[3]/ul[2]/li[4]/a",
                      "xpath_test_query": "//*[@id=\"body\"]/div/div/section[1]/div/h2//text()",
                      "xpath_test_result": ["\n    \n      Legalstart, le partenaire juridique de plus de 50 000 entrepreneurs\n    "],
                  },
            "ada91079": {
                      "next_page_expected": "d1786387",
                "xpath_button_to_click": "/html/body/div[1]/nav/div/div/ul/li[1]/div/div/div[1]/ul/li[6]/a",
                "xpath_test_query": "//*[@id=\"body\"]/div/div/div/div/div[1]/div[2]/h3//text()",
                "xpath_test_result": ["Formalit\u00e9s auto-entrepreneur"]
            },
        }
        scraper = ThumbScraper(url, pages)
        scraped_result  = scraper.scrape()
        assert scraped_result == ['Moved to page 1', "ALERT - can't move to page 2: page 1 link has been malevolently tampered withh!"]
