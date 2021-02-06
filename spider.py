# -*- encoding = utf-8 -*-
# @Time : 2021/2/4 22:50
# @Author : Liu
# @File : spider.py
# @Software : PyCharm

import urllib.request
from bs4 import BeautifulSoup
import re


#爬取网页
def getData(baseUrl):
    datalist = []
    for i in range(0,10):
        url = baseUrl + str(i*25)
        html = askURL(url)

        # 解析
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_ = "item"):
            print(item,"\n====================================\n")
            data = []
            item = str(item)

            link = re.findall(findLink,item)[0]
            data.append(link)

            imgSrc = re.findall(findImg,item)[0]
            data.append(imgSrc)

            title = re.findall(findTitle,item)
            if(len(title) == 2):
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace("/","")
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(" ")

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if(len(inq) != 0):
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?',"",bd)
            data.append(bd.strip())                     #去掉前后空格

            datalist.append(data)

        for item in datalist:
            print(item)




    #return datalist


def askURL(url):
    head = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        return html
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

def main():
    #爬取网页
    url = "https://movie.douban.com/top250?start="
    savePath = ".\\doubanMoviesTop250.xls"
    #askURL("https://movie.douban.com/top250?start=0")
    dataList = getData(url)






findLink = re.compile(r'<a href="(.*?)">')
findImg = re.compile(r'<img.*src="(.*?)"',re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

if __name__ == '__main__':
    main()
