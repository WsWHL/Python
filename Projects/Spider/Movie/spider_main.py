#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
import os
import re

import url_manager
import html_downloader
import html_parser
import html_output
import MyThread


class SpiderMain(object):
    """爬虫总调度程序"""

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3042.4 Safari/537.36"
        self.charset = "gb2312"
        self.file_path = "./Files/"
        self.maxThread = 6  # 默认设置最多同时运行6个线程
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader(self.user_agent, self.charset)
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print("正在获取第%s个页面数据：%s" % (str(count), new_url))
            html_cont = self.downloader.downloader(new_url)
            if html_cont is None or len(html_cont) <= 0:
                continue
            new_urls, new_data = self.parser.parser(root_url, html_cont)
            self.urls.add_new_urls(new_urls)
            if new_data is not None:
                print("电影名：" + new_data["title"])
                if len(new_data) > 2:
                    reobj = re.compile(r"(?:\\\\|/|:|\*|\?|<|>|\|)+")
                    result, number = reobj.subn(" ", new_data["title"])
                    img_path = self.file_path + "Images/" + str(result) + "/"
                    if not os.path.exists(img_path):
                        os.makedirs(img_path)
                    for url in new_data["img_urls"]:
                        thread = MyThread.Thread(target=self.downloader.downloader_files, args=(url, img_path))
                        while thread.get_threading_num() >= self.maxThread:
                            time.sleep(5)
                        thread.start()
            count += 1


if __name__ == "__main__":
    root_url = "http://www.dy2018.com"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)