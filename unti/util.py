# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def get_element(driver, *loc):
    return driver.find_element(*loc)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com')
    get_element(driver, By.ID, 'kw').send_keys('自动化')
    get_element(driver, By.ID, 'su').click()
    time.sleep(1)
    driver.quit()