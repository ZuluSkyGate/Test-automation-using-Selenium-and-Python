import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

icon = driver.find_element("class name", "wikipedia-search-wiki-link")
assert icon == icon, "Это не иконка википедии"
search_field = driver.find_element("id", "Wikipedia1_wikipedia-search-input")
assert search_field == search_field, "Это не поисковое поле"

search_button = driver.find_element("class name", "wikipedia-search-button")
assert search_button == search_button, "Это не кнопка поиска"

tag_name = driver.find_elements("tag name", "button")[0].click()

time.sleep(3)