#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2


class HtmlDownloader(object):
    """Html下载器"""

    def __init__(self):
        self.user_agent = None
        self.status = None

    def downloader(self, url):
        if url is None:
            return None
        request = urllib2.Request(url)
        if self.user_agent is not None:
            request.add_header("User-Agent", self.user_agent)
        response = urllib2.urlopen(request)
        self.status = response.getcode()
        if self.status != 200:
            return None
        return response.read()
