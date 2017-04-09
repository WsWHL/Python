#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import re
import gzip


class HtmlDownloader(object):
    """HTML下载器"""

    def __init__(self, user_agent, charset):
        self.__user_agent = user_agent
        self.__charset = charset
        self.status = None

    def downloader(self, url):
        if url is None:
            return
        request = urllib.request.Request(url)
        response = None
        if self.__user_agent is not None:
            request.add_header("User-Agent", self.__user_agent)
            request.add_header("Accept",
                               "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
            request.add_header("Accept-Encoding", "gzip, deflate, sdch")
        try:
            response = urllib.request.urlopen(request)
            self.status = response.getcode()
        except TimeoutError as err:
            print("请求超时：", err)
            return None
        except:
            print("在打开该链接时发生了未知异常，URL:", url)
            return None
        if self.status != 200:
            return None
        return gzip.decompress(response.read()).decode('gbk')

    def downloader_files(self, url, file_path):
        if url is not None and file_path is not None:
            name = re.compile(r"([^/][\dA-Za-z_]+\.(?:jpg|jpeg|png|gif))").findall(url)
            urllib.request.urlretrieve(url, file_path + name[0])
            return True
        return False
