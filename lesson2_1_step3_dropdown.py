
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = int(num1.text)

    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = int(num2.text)
    
    x_y = str(x+y)    

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x_y) # ищем элемент с текстом "Python"
    
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