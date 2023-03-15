from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()

try:
    driver.get(link)

    first_name = driver.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')
    first_name.send_keys("Sergei")

    last_name = driver.find_element(By.XPATH, './/input[@placeholder="Enter last name"]')
    last_name.send_keys("Biryukov")

    email = driver.find_element(By.XPATH, './/input[@placeholder="Enter email"]')
    email.send_keys("qwerty123456@gmail.com")

    file_name = "file.txt"
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file_name)
    element = driver.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = driver.find_element(By.XPATH, './/button[@type="submit"]')
    button.click()

finally:
    time.sleep(5)
    driver.quit()
