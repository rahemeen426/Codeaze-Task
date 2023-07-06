from selenium import webdriver
# Initialize the web driver
driver = webdriver.chrome.webdriver.WebDriver()  # Replace with the appropriate driver (e.g., Firefox)
# Open a website
driver.get("https://www.example.com")
# Perform actions or assertions
print(driver.title)
# Quit the browser
driver.quit()
