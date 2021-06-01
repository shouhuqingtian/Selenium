from selenium import webdriver
import time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')
        time.sleep(1)

    def test_id(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        # self.driver.quit()

    def test_name(self):
        self.driver.find_element_by_name('wd').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.driver.quit()

    def test_linktext(self):
        self.test_id()
        time.sleep(1)
        self.driver.find_element_by_link_text('百度首页').click()
        time.sleep(1)
        self.driver.quit()

    def test_partia_linktext(self):
        self.test_id()
        time.sleep(1)
        self.driver.find_element_by_partial_link_text('百度').click()
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_id()
    # case.test_name()
    case.test_partia_linktext()