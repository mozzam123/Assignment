from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time


url = "https://www.google.com/maps/search/stazioni+di+d/@43.9920058,10.9739238,10z?entry=ttu"

# Set up Chrome options to prevent the browser from closing after the script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Open the URL
driver.get(url)

# Maximize the Chrome window
driver.maximize_window()
time.sleep(1)
