#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

times = time.sleep(5)
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(5)
EC.title_contains("百度一下，你就知道")
# print(EC.title_contains("百度一下"))
# EC.visibility_of()
text = driver.find_element(By.ID, "kw")
text.send_keys("真好")
times

driver.find_element(By.ID, "su").click()
times
driver.find_element(By.ID, "kw").clear()
times

driver.find_element(By.ID, "kw").send_keys("python")
times
driver.find_element(By.ID, "su").click()

time.sleep(10)
driver.close()