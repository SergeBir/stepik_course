from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
driver = webdriver.Chrome()

try:

    driver.get(link)
    num1 = driver.find_element(By.XPATH, ".//span[@id='num1']")
    num1_text = num1.text
    num2 = driver.find_element(By.XPATH, ".//span[@id='num2']")
    num2_text = num2.text
    result = int(num1_text) + int(num2_text)

    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(result))

    button = driver.find_element(By.XPATH, './/button[@type="submit"]')
    button.click()

finally:
    time.sleep(5)
    driver.quit()


