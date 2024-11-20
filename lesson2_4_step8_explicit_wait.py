from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math



try:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Открывает браузер на полный экран 
    browser = webdriver.Chrome(options=options)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 
    # говорим Selenium дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = WebDriverWait(browser, 12).until(
        EC. text_to_be_present_in_element((By.ID, "price"), text_="$100")
    )
    
    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

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

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

    # Проверяем
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()