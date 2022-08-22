from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@name='firstname']")
    input1.send_keys('name')
    input2 = browser.find_element(By.XPATH, "//input[@name='lastname']")
    input2.send_keys('lastname')
    input3 = browser.find_element(By.XPATH, "//input[@name='email']")
    input3.send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)
    
    button1 = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button1.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()