class WebPage(object):

    def __init__(self, url, content, content_type):
        self._url = url
        self._content = content
        self._content_type = content_type
        self._tree = None

    def __repr__(self):
        return "WebPage({})".format(self._content)

    def parse(self):
        if self._tree is not None:
            return self._tree

        parser = Parser().get_parser(self._content_type)

        try:
            self._tree = etree.parse(self._content, parser)
        except Exception as e:
            raise WebPageParseException(e)

        return self._tree
