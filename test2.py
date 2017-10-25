from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    open = webdriver.Chrome(chrome_options = option)
    open.get("https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html")
    #assert "信息公开平台" in open.title
    #page = open.find_element_by_xpath("//a[@href='7027/default.htm']")
    #open.execute_script('arguments[0].scrollIntoView();', page[-1])
    #time.sleep(5)
    #page.click()
