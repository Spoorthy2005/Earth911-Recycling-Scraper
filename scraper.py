from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

print("Launching browser...")
driver = webdriver.Chrome()
driver.get("https://search.earth911.com/")

wait = WebDriverWait(driver, 15)

print("Waiting for search inputs to load...")
search_input = wait.until(EC.presence_of_element_located((By.ID, "what")))
search_input.clear()
search_input.send_keys("Electronics")

location_input = driver.find_element(By.ID, "where")
location_input.clear()
location_input.send_keys("10001")

print("Waiting for search button and clicking it...")
search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search__submit")))
search_button.click()

print("Waiting for results to load...")
time.sleep(5)

print("Scraping results...")
facilities = driver.find_elements(By.CLASS_NAME, "facility__container")

data = []

for facility in facilities[:3]:  # Limit to 3 facilities
    try:
        name = facility.find_element(By.CLASS_NAME, "facility__name").text.strip()
        address = facility.find_element(By.CLASS_NAME, "facility__address").text.strip()
        updated = facility.find_element(By.CLASS_NAME, "facility__last-update").text.strip()
        materials = facility.find_element(By.CLASS_NAME, "facility__materials").text.strip()

        print(f"✔ Found: {name}")
        data.append([name, updated, address, materials])
    except Exception as e:
        print("⚠ Error reading a facility:", e)

print("Saving to CSV...")
with open("facilities.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["business_name", "last_update_date", "street_address", "materials_accepted"])
    writer.writerows(data)

print("✅ Scraping complete. Data saved to 'facilities.csv'.")
driver.quit()
