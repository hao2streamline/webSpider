# -*- encoding = utf-8 -*-
# @Time : 2021/2/6 23:44
# @Author : Liu
# @File : aboutRe.py
# @Software : PyCharm

#正则表达式：字符串模式
import re

pat = re.compile("AA") #正则表达式
#m = pat.search("") #校验字符串
m = pat.search("ABCAA")
print(m)
#<re.Match object; span=(3, 5), match='AA'>
#在位置3-5（左闭右开）匹配

n = pat.search("ABCAAABCAA")
print(n)

#无模式对象
o = re.search("asd","Aasd")
print(o)

#findall
print(re.findall("[A-Z]+","ASDaDGAa"))

#sub
print(re.sub("a","A",r"abcdacsd"))
#在参数3中用参数2替换参数1