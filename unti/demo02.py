from selenium import webdriver
import time
from selenium.webdriver.common.by import By


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

    def test_xpath(self):
        self.driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys('极客时间')  # //*[@id="kw"]
        self.driver.find_element_by_xpath('//input[@value="百度一下"]').click()
        time.sleep(1)
        self.driver.quit()

    def test_tag(self):
        self.driver.find_element_by_tag_name('form')[0].sendkeys('极客时间')
        self.driver.find_element_by_xpath('//input[@value="百度一下"]').click()
        time.sleep(1)
        self.driver.quit()

    def test_css_selector(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('八大元素定位方式')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(1)
        self.driver.quit()

    def test_class(self):
        self.driver.find_element_by_class_name('s_ipt').send_keys('江西')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(1)
        self.driver.quit()

    def test_all(self):  # 定义自定义方式定位
        self.driver.find_element(By.ID, 'kw').send_keys('自动化测试')
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_id()
    # case.test_name()
    # case.test_partia_linktext()
    # case.test_xpath()
    # case.test_tag()
    # case.test_css_selector()
    # case.test_class()
    case.test_all()