from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    lines = driver.find_elements(By.XPATH, './/input[@type = "text"]')
    for line in lines:
        line.send_keys("Privet")

    button = driver.find_element(By.XPATH, './/button[@type = "submit"]')
    button.click()

finally:
    time.sleep(10)
    driver.quit()
