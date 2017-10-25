# -*- coding:UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib.parse
import time
import sys
import os


if __name__ == "__main__":
    b = b'/:?='
    url = 'http://m.kukudm.com/comiclist/2297/57424/1.htm'
    driver = webdriver.PhantomJS(executable_path='E:/ruanjian/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    content = driver.page_source
    html = BeautifulSoup(str(content),'lxml')
    name = '001.jpg'
    urls = html.find('img').get('src')
    print(urls)
    url1 = urllib.parse.quote(urls,b)
    print(url1)
    urlretrieve(url = url1,filename='cartoon/' + name)
    #print(url)

