from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    driver.get(link)
    x_element = driver.find_element(By.XPATH, './/img[@src="images/chest.png"]')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    line = driver.find_element(By.XPATH, './/input[@id="answer"]')
    line.send_keys(y)

    check_box = driver.find_element(By.XPATH, './/input[@type="checkbox"]')
    check_box.click()

    radio_button = driver.find_element(By.XPATH, './/input[@id="robotsRule"]')
    radio_button.click()

    button = driver.find_element(By.XPATH, './/button[@type="submit"]')
    button.click()

finally:
    time.sleep(5)
    driver.quit()