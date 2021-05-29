from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.find_element_by_class_name()