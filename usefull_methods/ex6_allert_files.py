from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
driver = webdriver.Chrome()

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    driver.get(link)

    button = driver.find_element(By.XPATH, './/button[@type="submit"]')
    button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    x_element = driver.find_element(By.XPATH, './/span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    line = driver.find_element(By.XPATH, './/input[@class="form-control"]')
    line.send_keys(y)

    button_confirm = driver.find_element(By.XPATH, './/button[@type="submit"]')
    button_confirm.click()

finally:
    time.sleep(11)
    driver.quit()

