from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Launch the web browser
driver = webdriver.Chrome()
# Open Google Meet link
meeting_link = "https://meet.google.com/ecm-okyf-ofm?authuser=0&hs=122"
driver.get(meeting_link)
# Wait for the "Join" button to be clickable
join_button_locator = (By.XPATH, "//span[text()='Join']")
join_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(join_button_locator)
)
# Click the "Join" button
join_button.click()
# Close the web browser
driver.quit()