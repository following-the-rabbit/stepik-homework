import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))

    num1 = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(num1.text)
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()


    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()