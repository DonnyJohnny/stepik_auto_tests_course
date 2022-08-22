from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    x2 = browser.find_element(By.CSS_SELECTOR, "#num2").text

    l = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    l.select_by_value(str(int(x1) + int(x2)))


    button1 = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button1.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()