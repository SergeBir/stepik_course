from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()

try:

    browser.get(link)

    first_name = browser.find_element(By.XPATH, './/input[@name="first_name"]')
    second_name = browser.find_element(By.XPATH, './/input[@name="last_name"]')
    city = browser.find_element(By.XPATH, './/input[@class="form-control city"]')
    country = browser.find_element(By.XPATH, './/input[@id="country"]')
    button = browser.find_element(By.XPATH, './/button[@id="submit_button"]')

    first_name.send_keys("Sergei")
    second_name.send_keys("Biryukov")
    city.send_keys("Smolensk")
    country.send_keys("Russia")
    button.click()

finally:
    time.sleep(4)
    browser.quit()
