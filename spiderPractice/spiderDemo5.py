#coding:utf-8

#用selenium 通过用户名和账号自动获取cookie
#https://weibo.cn/ 不同于m站

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait    #等待页面加载某些元素
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   #按照什么方式查找，By.ID,By.CSS_SELECTOR

def get_cookie_from_weibo(username, password):
    driver = webdriver.Chrome()
    driver.get('https://weibo.cn/')
    assert "微博" in driver.title
    login_link = driver.find_element_by_link_text('登录')
    ActionChains(driver).move_to_element(login_link).click().perform()
    login_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginName"))
    )
    login_password = driver.find_element_by_id("loginPassword")
    login_name.send_keys(username)
    login_password.send_keys(password)
    login_button = driver.find_element_by_id("loginAction")
    login_button.click()
    cookie = driver.get_cookies()
    driver.close()
    #return cookie
    print(cookie)
get_cookie_from_weibo(13810962072,'Welcome2sohu')
