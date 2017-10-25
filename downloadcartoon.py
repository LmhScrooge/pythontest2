from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve
from urllib import request
from selenium import webdriver
import re
import urllib.parse
import socket
import datetime

if __name__ == "__main__":
    b = b'/:?='
    socket.setdefaulttimeout(10)
    url = 'http://comic.kukudm.com/comiclist/2297/index.htm'
    driver = webdriver.PhantomJS(executable_path='E:/ruanjian/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    list_url_req = requests.get(url = url,headers = head)
    list_url_req.encoding = 'gbk'
    list_url_html = BeautifulSoup(list_url_req.text,'lxml')
    list_url_text = list_url_html.find_all('dl',id = 'comiclistn')
    list_url = BeautifulSoup(str(list_url_text),'lxml')
    #找出漫画所有卷
    dirs = list_url.find_all('dd')
    for each in dirs:
        #漫画每一卷的链接
        cartoon_url = 'http://comic.kukudm.com' + each.a.get('href')
        cartoon_url.split('/')
        #漫画每一卷名字
        cartoon_name = each.a.string
        #为每一卷创建一个文件夹
        cartoon_file = 'cartoon/'+cartoon_name
        os.makedirs(cartoon_file)
        #获取每一卷的页数
        cartoonurl_req = requests.get(url = cartoon_url,headers = head)
        cartoonurl_req.encoding = 'gbk'
        cartoon_number = int(re.compile('共(\d+)页').findall(cartoonurl_req.text)[0])
        time1 = datetime.datetime.now()
        for i in range(1,cartoon_number+1):
            carurl =cartoon_url[:-5] + str(i) + '.htm'
            try:
                driver.get(carurl)
            except socket.timeout:
                print('error')
                continue
            html = BeautifulSoup(str(driver.page_source),'lxml')
            download_url = html.find('img').get('src')
            download_urls = urllib.parse.quote(download_url,b)
            picname = str(i) + '.jpg'
            try:
                urlretrieve(url = download_urls,filename = cartoon_file + '/' +picname)
                print("正在下载", cartoon_name, ":第", i, "页")
            except socket.timeout:
                print(cartoon_name,":第",i,"页下载失败")
        time2 = datetime.datetime.now()
        print("共耗时：",time2 - time1)