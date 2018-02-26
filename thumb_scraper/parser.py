from lxml import etree

from thumb_scraper.exceptions import *


class Parser(object):

    def __init__(self):
        self.parser = {
            "text/html": etree.HTMLParser(),
        }

    def get(self, doc_type):
        if doc_type not in self.parser:
            raise PaserNotFoundException("{} parser is not available".format(doc_type))

        return self.parser[doc_type]
