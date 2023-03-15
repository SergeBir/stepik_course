from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
incorrect_link = "http://suninjuly.github.io/registration2.html"  # При проверке по первой ссылке столкнемся с ошибкой
correct_link = "http://suninjuly.github.io/registration1.html"  # При проверке по второй ссылке тест пройдет успешно

try:
    browser.get(incorrect_link)

    first_name = browser.find_element(By.XPATH, './/input[@placeholder="Input your first name"]')
    first_name.send_keys("Sergei")

    last_name = browser.find_element(By.XPATH, './/input[@placeholder="Input your last name"]')
    last_name.send_keys("Biryukov")

    email = browser.find_element(By.XPATH, './/input[@placeholder="Input your email"]')
    email.send_keys("qwerty123456@gmail.com")

    button = browser.find_element(By.XPATH, './/button[@type="submit"]')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
