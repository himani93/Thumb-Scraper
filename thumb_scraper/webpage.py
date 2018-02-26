from lxml import etree
from io import StringIO

from thumb_scraper.exceptions import *
from thumb_scraper.parser import Parser


class WebPage(object):

    def __init__(self, url, content="", content_type="", encoding="utf-8"):
        if not url:
            raise InvalidURLException("{} is not valid url".format(url))
        self._url = url
        self._content = content
        self._content_type = content_type
        self._encoding = encoding
        self._tree = None

    def __repr__(self):
        return "WebPage({})".format(self._content[:10])

    def parse(self):
        if self._tree is not None:
            return self._tree

        parser = Parser().get(self._content_type)

        try:
            self._tree = etree.parse(StringIO(unicode(self._content, self._encoding)), parser)
        except Exception as e:
            raise WebPageParseException(e)

        print etree.tostring(self._tree)
        return self._tree

    def evaluate_query(self, query):
        webpage_tree = self.parse()
        try:
            query_result = webpage_tree.xpath(query)
        except Exception as e:
            raise EvaluateQueryException(e)

        return query_result

    def is_tampered(self, query, result):
        evaluated_result = self.evaluate_query(query)
        print evaluated_result, result
        return False if evaluated_result == result else True
