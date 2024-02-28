from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time

url = "https://stores.cartier.com/it/search?q=&category=storeLocatorSearch&r=10&storetype=false"

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

# Locate the button using XPath and click on it
button_xpath = "/html/body/div[1]/div/div[2]/button[1]"
button = driver.find_element(By.XPATH, button_xpath)
button.click()
time.sleep(3)

# Locate the search input field and type 'London'
search_input_xpath = "/html/body/main/div/div[4]/div[1]/div/div[1]/form/input"
search_input = driver.find_element(By.XPATH, search_input_xpath)
search_input.send_keys("London")

# Wait for a while to see the result (you can adjust the time as needed)
time.sleep(3)

# Locate the search button using XPath and click on it
search_button_xpath = "/html/body/main/div/div[4]/div[1]/div/div[1]/form/div/div[3]/a"
search_button = driver.find_element(By.XPATH, search_button_xpath)
search_button.click()

# Wait for a while to ensure the search results are loaded (you can adjust the time as needed)
time.sleep(5)

# Locate all the addresses on the page (modify the XPath accordingly)
address_elements = driver.find_elements(By.XPATH, "/html/body/main/div[2]/section/div[2]/ul")

# Create a list to store the addresses
addresses = []

# Extract and store the addresses in the list
for address_element in address_elements:
    address_text = address_element.text
    print("address_text: ", address_text)
    addresses.append(address_text)

# Save addresses to a CSV file
csv_file_path = "addresses.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    for address in addresses:
        csv_writer.writerow([address])

# Print a message indicating the CSV file has been created
print(f"Addresses have been saved to {csv_file_path}")

# Remember to close the browser when you are done (manually or programmatically)
# driver.quit()
