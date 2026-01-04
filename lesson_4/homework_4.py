import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

driver.get("https://vk.com/")

current_title = driver.title
print("Текущий заголовок: ", current_title)
assert current_title == "ВКонтакте | Добро пожаловать", "Некорректный заголовок страницы"

time.sleep(3)

driver.get("https://www.wikipedia.org/")

url = driver.current_url
print("URL страницы: ", url)
assert url == "https://www.wikipedia.org/", "Ошибка в URL, открыта неверная страница сайта."

time.sleep(10)

driver.back()

time.sleep(3)

driver.refresh()

url = driver.current_url
print("URL страницы: ", url)

time.sleep(3)

driver.forward()

url = driver.current_url
print("URL страницы: ", url)

driver.quit()