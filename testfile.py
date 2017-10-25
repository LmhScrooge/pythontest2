from selenium import webdriver
import datetime
import time
import profile

if __name__ == "__main__":
    logname = open("log.txt", 'a')
    nowtime = str(datetime.datetime.now())
    logname.write(nowtime + ":successful" + '\n')