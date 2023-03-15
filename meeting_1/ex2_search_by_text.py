from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
driver = webdriver.Chrome()

try:
    driver.get(link)
    math_result = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    line_by_text = driver.find_element(By.PARTIAL_LINK_TEXT, str(math_result))
    line_by_text.click()

    first_name = driver.find_element(By.XPATH, './/input[@name="first_name"]')
    first_name.send_keys("Sergei")
    second_name = driver.find_element(By.XPATH, './/input[@name="last_name"]')
    second_name.send_keys("Biryukov")
    city = driver.find_element(By.XPATH, './/input[@class="form-control city"]')
    city.send_keys("Smolensk")
    country = driver.find_element(By.XPATH, './/input[@id="country"]')
    country.send_keys("Russia")
    button = driver.find_element(By.XPATH, './/button[@type="submit"]')
    button.click()


finally:
    time.sleep(5)
    driver.quit()
