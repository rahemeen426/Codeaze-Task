from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver =  webdriver.chrome.webdriver.WebDriver()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("Hello World", Keys.ENTER)
input()
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()