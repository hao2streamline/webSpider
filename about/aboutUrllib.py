# -*- encoding = utf-8 -*-
# @Time : 2021/2/4 22:10
# @Author : Liu
# @File : aboutUrllib.py
# @Software : PyCharm

import urllib.response
import urllib.parse
import urllib.request


#获取get请求
# response = urllib.request.urlopen("https://baidu.com")
# print(response.read().decode('UTF-8'))

#获取post请求
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode('UTF-8'))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('UTF-8'))
# except urllib.error.URLError as e:
#     print("time out")

#编辑response head

# response = urllib.request.urlopen("https://baidu.com")
# #print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))

# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"name":"liu"}),encoding="utf-8")
# heders = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
# }
#
# req = urllib.request.Request(url=url,data=data,headers=heders,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


# url = "http://douban.com"
# heders = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
# }
# req = urllib.request.Request(url=url,headers=heders,method="GET")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))