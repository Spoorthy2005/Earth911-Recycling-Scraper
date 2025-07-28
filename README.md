# Earth911-Recycling-Scraper

## 🔧 Libraries Used
- **Selenium** – To interact with the dynamic Earth911 search page
- **BeautifulSoup** – To parse HTML and extract data cleanly
- **CSV** – For structured data output
- **Time** – Basic delay to ensure page loads before parsing

## 🧠 Scraping Logic
1. Open Earth911’s search result using Selenium.
2. Wait for the JavaScript to render results.
3. Use BeautifulSoup to extract the first 3 facility cards.
4. Extract:
   - Business Name
   - Last Update Date
   - Street Address
   - Materials Accepted
5. Save everything into a structured CSV.

## 🔁 Pagination Handling
- Currently only handles the first page.
- Can be extended by identifying the pagination component in the DOM and iterating over pages.

## 🧹 Data Cleaning
- `.strip()` used to clean whitespace.
- Materials accepted are extracted and joined using commas.

## ⚠️ Error Handling
- Try/except block while extracting each facility to skip missing fields and continue the script.

## 🏆 Bonus Task (BestBuy Store Locator)
If included:
- Use BestBuy’s ZIP-based locator at: https://www.bestbuy.com/site/store-locator
- Plan:
  - Use Selenium to enter ZIP code 10001 and press search.
  - Extract store names, addresses, hours.
  - Output to CSV.

## 🧩 Proposed Improvements
- Add logging and exception tracing.
- Handle multiple pages (pagination logic).
- Extend support for multiple ZIP codes using loops.

