from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

url = 'https://www.iotindiaexpo.com/exhibitors-and-participants.aspx'

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Wait for the dynamic content to load
time.sleep(2)

data = []

# Loop through each page
while True:
    # Extract table data on the current page
    table = driver.find_element(By.ID, 'example')  # Replace with the correct ID
    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        cols = row.find_elements(By.TAG_NAME,'td')
        data.append([col.text for col in cols])

    # Find the next page button and click it
    try:
        next_page_button = driver.find_element(By.CLASS_NAME,'next')  # Replace with the correct ID or class
          # Print information about the button
        print("Button Text:", next_page_button.text)
        print("Button ID:", next_page_button.get_attribute('id'))
        print("Button Class:", next_page_button.get_attribute('class'))
        if 'disabled' in next_page_button.get_attribute('class'):
         print("Reached the last page. Exiting loop.")
         break
        else:
         next_page_button.click()
         time.sleep(2)  # Wait for page to load
         # Wait for page to load
    except Exception as e:
        print("Exception occurred:", e)
        # If no more pages, break the loop
        break

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_excel('participants_list.xlsx', index=False)

# Close the WebDriver
driver.quit()
