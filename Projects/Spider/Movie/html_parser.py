#! /usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import parse
import re


class HtmlParser(object):
    """HTML解析器"""

    def __get_new_urls(self, page_url, html_cont):
        new_urls = set()
        a_urls = re.findall(r"<a href=['|\"](/i/\d+\.html)['|\"].*?>.*?</a>", html_cont)
        if a_urls is not None:
            for url in a_urls:
                new_urls.add(parse.urljoin(page_url, url))

        return new_urls

    def __get_new_data(self, page_url, html_cont):
        res_data = {}
        title = re.findall(r"<div class=\"title_all\"><h1>(.*?)</h1></div>", html_cont)
        urls = re.findall(r"<a href=\"(ftp://.*?)\">.*?</td>", html_cont)
        img_urls = re.findall(r"<img.*?src=\"(http://.*?)\".*?>", html_cont)
        if title is None or len(title) <= 0 or urls is None or len(urls) <= 0:
            return
        if re.search(r"title", title[0]) is not None:
            return None
        res_data["title"] = title[0]
        res_data["file_urls"] = urls
        if img_urls is not None and len(img_urls) > 0:
            res_data["img_urls"] = img_urls

        return res_data

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        new_urls = self.__get_new_urls(page_url, html_cont)
        new_data = self.__get_new_data(page_url, html_cont)
        return new_urls, new_data
