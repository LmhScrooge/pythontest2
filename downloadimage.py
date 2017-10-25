from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
from selenium import webdriver

if __name__ == "__main__":
    img_url = []
    #爬取多少个页面上的照片
    for flag in range(1,2):
        if flag == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html'%flag
        head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        req = requests.get(url = url,headers = head)
        req.encoding = 'utf-8'
        html = req.text
        txt = BeautifulSoup(str(html),'lxml')
        imgtxt = txt.find_all(class_="item-img")
        for each in imgtxt:
            img_url.append(each.img.get('alt') + "=" + each.get('href'))
    for every in img_url:
        target = every.split('=')
        imgname = target[0] + '.jpg'
        imgurl = target[1]
        imgreq = requests.get(url = imgurl,headers = head)
        imgreq.encoding = 'utf-8'
        imghtml = imgreq.text
        imgtext = BeautifulSoup(imghtml,'lxml')
        dltext = imgtext.find_all(class_="wr-single-content-list")
        dltxt = BeautifulSoup(str(dltext),'lxml')
        dlurl = 'http://www.shuaia.net' + dltxt.img.get('src')
        urlretrieve(url=dlurl, filename='images/' + imgname)
        print(dlurl + "下载完成")
