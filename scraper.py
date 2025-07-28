import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Setup headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://search.earth911.com/?what=Electronics&where=10001&list_filter=all&max_distance=100&country=US&latitude=40.7507428&longitude=-73.99653&region=NY&page=1"
driver.get(url)

time.sleep(5)  # wait for JS content to load

# Scrape results
soup = BeautifulSoup(driver.page_source, 'html.parser')

facility_cards = soup.select('.MuiPaper-root.MuiCard-root')[:3]

data = []
for card in facility_cards:
    try:
        name = card.select_one('.MuiTypography-h6').text.strip()
        address = card.select_one('[data-testid="address"]').text.strip()
        last_updated = card.select_one('[data-testid="updateDate"]').text.strip()
        materials = ", ".join([tag.text.strip() for tag in card.select('[data-testid="materialTag"]')])
        
        data.append([name, last_updated, address, materials])
    except Exception as e:
        print(f"Error: {e}")

driver.quit()

# Save to CSV
with open('facilities.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["business_name", "last_update_date", "street_address", "materials_accepted"])
    writer.writerows(data)
