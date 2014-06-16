# -*- coding: utf-8 -*-
__author__ = 'eternnoir'
import httplib2
import urllib


try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError(
            "You need to have a json parser, easy_install simplejson")


class Googl:

    """
    Goo.gl shorten service
    """

    def __init__(
            self,
            apiKey=None,
            baseUrl='https://www.googleapis.com/urlshortener/v1/url',
            agent='python-google'):
        self.apiKey = apiKey
        self.baseUrl = baseUrl
        self.httpConn = httplib2.Http()
        self.agent = agent
        return

    def _request(
            self,
            url="",
            method="GET",
            body="",
            headers=None,
            userip=None):
        """send request and parse the json returned"""
        if not url:
            url = self.baseUrl
        elif not url.startswith("http"):
            url = "%s?%s" % (self.baseurl, url)
        if self.apiKey is not None:
            url += "%s%s" % (("?" if "?" not in url else "&"),
                             "key=%s" % self.apiKey)
        if userip:
            url += "%s%s" % (("?" if "?" not in url else "&"),
                             "userip=%s" % userip)
        if headers is None:
            headers = {}
        if "user-agent" not in headers:
            headers['user-agent'] = self.agent
        return json.loads(
            self.httpConn.request(
                url,
                method,
                body=body,
                headers=headers)[1])

    def _shorten(self,url,userip = None):
        """Gen Short Url"""
        body = json.dumps(dict(longUrl=url))
        headers = {'content-type': 'application/json'}
        return self._request(
            method="POST",
            body=body,
            headers=headers,
            userip=userip)


    def getShortUrl(self,url,userip = None):
        return self._shorten(url,userip)['id']
