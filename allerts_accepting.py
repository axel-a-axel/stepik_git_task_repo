from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, '//button')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(x_element)
    field1 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    field1.send_keys(y)

    button = browser.find_element(By.XPATH, '//button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()