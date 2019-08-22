'''
Created on 2018年9月13日

@author: JinLian
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("https://cn.bing.com/")

# elements = pq(driver.page_source).find('.menu-item')
# # elements.length == 5
# print(elements)
# print(elements.length == 5)
# print(elements('li'))
# elements[1].text() == 'API Documentation'

# searchBox = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
# searchBox.send_keys(u"jquery 官网")
# searchBox.send_keys(Keys.control(), 'a')
#
# searchButton = driver.find_element_by_xpath('//*[@id="sb_form_go"]').click()
#
# wait = WebDriverWait(driver, 30)
# wait.until(lambda x: x.find_element_by_xpath(
#     '//*[@id="b_results"]/li[4]/h2/a'))
#
# print('页面加载完成')
# driver.close()


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 输入关键词内容
searchBox = driver.find_element_by_id("kw")
searchBox.send_keys("selenium")
searchButton = driver.find_element_by_xpath('//*[@id="su"]').click()
# print(searchBox)

wait = WebDriverWait(driver, 20)
wait.until(lambda x: x.find_element_by_xpath(
    '//*[@id="2"]/h3/a'))
# 删除键
searchBox.clear()

searchBox.send_keys("python")
# 空格键
searchBox.send_keys(Keys.SPACE)
# 输入内容
searchBox.send_keys("教程")
# 全选(Ctrl+A)
searchBox.send_keys(Keys.CONTROL, 'a')
# 剪切(Ctrl+X)
searchBox.send_keys(Keys.CONTROL, 'x')

driver.get('https://cn.bing.com/')
searchBox = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
# 粘贴(Ctrl+V)
searchBox.send_keys(Keys.CONTROL, 'v')
# 回车键
searchBox.send_keys(Keys.ENTER)

driver.find_element_by_id('sb_form_go').submit()

print(driver.find_element_by_id('est_cn').text)
print(searchBox.get_attribute('title'))
