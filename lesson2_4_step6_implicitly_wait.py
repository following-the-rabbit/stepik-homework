from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button")     
    # нет такого айдишника на странице

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()