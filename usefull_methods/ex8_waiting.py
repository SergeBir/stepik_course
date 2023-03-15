from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    driver.get(link)

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, './/h5[@id="price"]'), "$100"))

    button = driver.find_element(By.XPATH, './/button[@id="book"]')
    button.click()

    x_element = driver.find_element(By.XPATH, './/span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    line = driver.find_element(By.XPATH, './/input[@class="form-control"]')
    line.send_keys(y)

    button_confirm = driver.find_element(By.XPATH, './/button[@type="submit"]')
    button_confirm.click()

finally:
    time.sleep(7)
    driver.quit()
