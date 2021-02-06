# -*- encoding = utf-8 -*-
# @Time : 2021/2/4 23:08
# @Author : Liu
# @File : aboutBs4.py
# @Software : PyCharm

'''
Beautiful Soup将复杂的HTML文档转化成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种：
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''

from bs4 import BeautifulSoup
import re

file = open("../html/baidu.html", encoding="utf-8")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

#1.Tag 找到的第一个标签及其内容
print(bs.title)
print(bs.a)
print(bs.head)
print(type(bs.head))

#2.NavigableString 标签里的内容
print(bs.title.string)
print(type(bs.title.string))

#attrs标签里的所有属性
print(bs.a.attrs)
print(type(bs.a.attrs))

#3.BeautifulSoup表示整个文档
print(type(bs))

#4.Comment特殊的NavigableString，不包含注释
print(bs.a.string)
print(type(bs.a.string))

########################################################################################################################
#文档的遍历
print("########################")
print(bs.head.contents)
print(bs.head.contents[1])

#文档的搜索
#1.find all

#1.1 字符串过滤
#t_list = bs.find_all("a")

#1.2正则表达式搜索：使用search（）
t_list = bs.find_all(re.compile("a"))

#1.3.方法：传入一个函数（方法），根据函数要求搜搜
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)

#2.keywords 参数
t_list = bs.find_all(id = "head")
t_list = bs.find_all(class_ = "True")

#3.text参数
t_list = bs.find_all(text="hao123")

t_list = bs.find_all(text=["hao123","贴吧","地图"])

t_list = bs.find_all(text= re.compile("\d"))  #正则表达式查找包含特定（数字）字符串文本的内容

#4.limt参数
t_list = bs.find_all("a",limit=3)



#CSS选择器
print(bs.select('title'))   #通过标签

t_list = bs.select(".mnav")#通过类名

t_list = bs.select("#u1")   #通过id

t_list = bs.select("a[calss = 'bri']") #通过属性

t_list = bs.select("head > title") #通过子标签 （兄弟节点、父节点）

# t_list = bs.select("。mnav ~ 。bri")
#
# print(t_list[0].get_text)

for item in t_list:
    print(item)