#! /usr/bin/env python
# -*- coding:utf-8 -*-


class UrlManager(object):
    """url管理器"""

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):  # 添加一个新的url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):  # 添加一组新的url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  # 判断是否有待爬取的url
        return len(self.new_urls) != 0

    def get_new_url(self):  # 获取一个带爬取的url,并将其添加到已爬取对象里面
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
