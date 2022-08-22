from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    cbx = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    cbx.click()

    rbn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rbn)
    rbn.click()

    button1 = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()