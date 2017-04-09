#! /usr/bin/env python
# -*- coding:utf-8 -*-


from PIL import Image
import requests
import re
import time
import os
import json

headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3061.0 Safari/537.36"
}

# 使用登录cooick信息
session = requests.session()


# 经测试发现知乎网站每次登录cookice会随登录时间的不同而发生编号，所以不能保存上一次登录获取到的cookice信息再次进行登录
# session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
# try:
#     print(session.cookies)
#     session.cookies.load(ignore_discard=True)
# except:
#     print("还没有cookie信息！")


# 获取登录页面的xsrf值
def get_xsrf():
    response = session.get("http://www.zhihu.com", headers=headers)
    xsrf = re.compile(r'<input.*?_xsrf.*?value=[\'"]([\da-z]+?)[\'"].*?').finditer(response.content.decode('utf-8'))
    return xsrf


# 获取登录的验证码（可以人工识别，也可使用第三方支持库来自动识别pytesser）
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r=" + t + "&type=login"
    response = session.get(captcha_url, headers=headers)
    with open("captcha.png", 'wb') as f:
        f.write(response.content)
    img = Image.open("captcha.png")
    img.show()
    captcha = input("请输入验证码：")
    return captcha


def login(userid, password):
    login_url = "https://www.zhihu.com/login/phone_num"
    form_data = {
        "phone_num": userid,
        "password": password,
        "captcha": get_captcha(),
        "_xsrf": get_xsrf()
    }
    response = session.post(login_url, data=form_data, headers=headers)
    login_code = response.json()
    return login_code


if __name__ == "__main__":
    userid = None
    password = None
    if not os.path.isfile("user.json"):
        userid = input("请输入手机号或邮箱：")
        password = input("请输入登录密码：")
    else:
        with open("user.json", "r") as f:
            user = json.loads(f.read())
            userid = user["userid"]
            password = user["password"]
    login_code = login(userid, password)
    print(login_code["msg"])
    if login_code["r"] == 0:
        open("user.json", "w+").write(
            "{\"userid\":\"%s\", \"password\":\"%s\", \"login_time\":\"%s\"}" % (
                userid, password, time.ctime(time.time())))
