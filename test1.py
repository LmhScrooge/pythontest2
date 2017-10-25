from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')
    assert "百度" in browser.title
    elem = browser.find_element_by_name("wd")
    elem.send_keys("python")
    elem.send_keys(Keys.RETURN)
    #print(browser.page_source)