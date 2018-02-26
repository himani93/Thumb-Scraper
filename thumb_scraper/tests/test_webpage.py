import pytest

from lxml import etree
from io import StringIO

from thumb_scraper.exceptions import *
from thumb_scraper.parser import Parser
from thumb_scraper.webpage import WebPage


class TestWebPage(object):

    def test_webpage_instance_if_url_invalid(self):
        url = ""
        content = "<html></html>"
        content_type = "text/html"

        with pytest.raises(InvalidURLException):
            WebPage(url, content, content_type)

    def test_webpage_instance_default_values(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com"

        web_page = WebPage(url)
        assert web_page._url == url
        assert web_page._content == ""
        assert web_page._content_type == ""
        assert web_page._tree == None

    def test_webpage_instance(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com"
        content = "<html></html>"
        content_type = "text/html"

        web_page = WebPage(url, content, content_type)
        assert web_page._url == url
        assert web_page._content == content
        assert web_page._content_type == content_type
        assert web_page._tree == None

    def test_webpage_repr(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com"
        content = "<html></html>"
        content_type = "text/html"

        web_page = WebPage(url, content, content_type)
        assert repr(web_page) == "WebPage({})".format(content[:10])

    def test_parse_web_page(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com"
        content = "<html><head><title>test<body><h1>page title</h3>"
        content_type = "text/html"

        html_parser = Parser().get(content_type)
        web_page = WebPage(url, content, content_type)
        web_page.parse()
        assert isinstance(web_page._tree, etree._ElementTree) == True
        assert etree.tostring(web_page._tree) == etree.tostring(etree.parse(StringIO(unicode(content)), html_parser))

    # def test_parse_web_page_exception(self):
    #     url = "https://yolaw-tokeep-hiring-env.herokuapp.com"
    #     content = "</td>"
    #     content_type = "text/html"

    #     html_parser = Parser().get(content_type)
    #     web_page = WebPage(url, content, content_type)
    #     with pytest.raises(WebPageParseException):
    #         web_page.parse()

    def test_evaluate_query(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com"
        content = "<html><head><title>test<body><h1>page title</h3>"
        content_type = "text/html"

        html_parser = Parser().get(content_type)
        web_page = WebPage(url, content, content_type)

        assert web_page.evaluate_query("//text()") == ["test", "page title"]

        with pytest.raises(EvaluateQueryException):
            web_page.evaluate_query("")

    def test_check_webpage_tampered(self):
        url = "https://yolaw-tokeep-hiring-env.herokuapp.com"
        content = "<html><head><title>test<body><h1>page title</h3>"
        content_type = "text/html"

        html_parser = Parser().get(content_type)
        web_page = WebPage(url, content, content_type)

        assert web_page.is_tampered("//text()", ["test", "page title"]) == False
        assert web_page.is_tampered("//text()", ["test"]) == True
