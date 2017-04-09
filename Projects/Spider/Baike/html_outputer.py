#! /usr/bin/env python
# -*- coding:utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # ascii
    def outputer_html(self):
        fout = open('output.html', 'w')
        fout.write("<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"></head><body><table>")
        fout.write("<tr><th>地址</th><th>标题</th><th>内容</th></tr>")
        for data in self.datas:
            fout.write("<tr>")
            if data['url'] is not None:
                fout.write("<td>%s</td>" % data['url'])
            else:
                fout.write("<td>None</td>")
            if data['title'] is not None:
                fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            else:
                fout.write("<td>None</td>")
            if data['summary'] is not None:
                fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            else:
                fout.write("<td>None</td>")
            fout.write("</tr>")
        fout.write("</table></body></html>")
