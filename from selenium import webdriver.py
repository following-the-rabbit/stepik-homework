from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Открывает браузер на полный экран

# Инициализация драйвера
driver = webdriver.Chrome(options=options)
driver.get("https://google.com")