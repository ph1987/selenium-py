from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("https://www.anitta.com.br/contato/")

elem = driver.find_element("name", "us_form_1_text_1")
elem.clear()
elem.send_keys("Neymar")

elem = driver.find_element("name", "us_form_1_email_1")
elem.clear()
elem.send_keys("neymarjr@gmail.com")

elem = driver.find_element("name", "us_form_1_textarea_1")
elem.clear()
elem.send_keys("Oi razão da minha libido rsrs")

elem = driver.find_element("name", "us_form_1_captcha_1")
elem.clear()
elem.send_keys("6")

sleep(10)

elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source