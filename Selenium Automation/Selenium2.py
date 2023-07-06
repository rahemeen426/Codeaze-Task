from selenium import webdriver
# Initialize the web driver
driver = webdriver.chrome.webdriver.WebDriver()  # Replace with the appropriate driver (e.g., Firefox)
# Open a website
driver.get("https://meet.google.com")
# Scroll by a specific pixel value
driver.execute_script("window.scrollBy(0, 5000);")
input()
# Quit the browser
driver.quit()