from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    input1.send_keys("123")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    input2.send_keys("456")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    input3.send_keys("789")


    # input4 = browser.find_element(By.CSS_SELECTOR, '#file')
    # input4.send_keys("789")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    
    ...

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()