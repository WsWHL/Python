#! /usr/bin/env python
# -*- coding:utf-8 -*-

import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    """爬虫总调度程序"""

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.downloader.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3025.0 Safari/537.36"

    def craw(self, roo_url):
        self.urls.add_new_url(roo_url)
        count = 0
        while self.urls.has_new_url() and count < 200:
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.downloader(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            count += 1
            print "已获取第%s个页面的内容---地址：%s" % (str(count), new_url.encode('utf-8'))
        self.outputer.outputer_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
