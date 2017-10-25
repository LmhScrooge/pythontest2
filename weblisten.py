from selenium import webdriver
import datetime
import time
import profile

if __name__ == "__main__":
    flag = True
    url = 'http://nxgov.com/zfmh/index.html'
    while flag :
        nowtime = str(datetime.datetime.now())
        web = webdriver.PhantomJS(executable_path='E:/ruanjian/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        try:
            web.set_page_load_timeout(5)
            web.get(url)
            print(nowtime, ':successful')
            logname = open("log.txt", 'a')
            logname.write(nowtime + ":successful" + '\n')
            logname.close()
            time.sleep(5)
            web.close()
            time.sleep(5)
        except:
            print(nowtime, ':error')
            logname = open("log.txt", 'a')
            logname.write(nowtime +":error" + '\n')
            logname.close()
            web.close()
            time.sleep(5)