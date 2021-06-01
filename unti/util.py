# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com')
    time.sleep(1)
    get_element(driver, By.ID, 'kw').sendkeys('自动化')
    get_element(driver, By.ID, 'su').click()