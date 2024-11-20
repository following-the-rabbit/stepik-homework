from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    # нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # узнаем имя новой вкладки 
    new_window = browser.window_handles[1]
    # явно переключаемся на новую вкладку
    browser.switch_to.window(new_window)

    # функции для расчета
    def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
    
    # выделяем поле со значением , которое нужно преобразовать
    num1 = browser.find_element(By.CSS_SELECTOR, '#input_value') 
    # присваеваем x значение из переменой num1 
    x = int(num1.text)
    # расчитываем y по x
    y = calc(x)

    # вводим значение у в поле для ответа
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
       
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