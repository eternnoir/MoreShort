# -*- coding: utf-8 -*-
__author__ = 'eternnoir'
import urllib


class tinyUrl:

    """Tiny Url short url service"""

    def __init__(
            self,
            apiurl="http://tinyurl.com/api-create.php?url=",
            ):
        self.apiUrl = apiurl

    def _shorten(self, url):
        """Gen Short Url
        :rtype : basestring
        """
        tinyurl = urllib.urlopen(self.apiUrl + url).read()
        return tinyurl

    def getShortUrl(self, url):
        """Get Short Url"""
        return self._shorten(url)
