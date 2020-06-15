from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("https://www.anitta.com.br/contato/")

elem = driver.find_element_by_name("name")
elem.clear()
elem.send_keys("Neymar")

elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("neymarjr@gmail.com")

elem = driver.find_element_by_name("message")
elem.clear()
elem.send_keys("Oi razão da minha libido rsrs")

elem = driver.find_element_by_name("captcha")
elem.clear()
elem.send_keys("17")

elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source