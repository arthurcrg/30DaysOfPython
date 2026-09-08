# Web Scrapping using BeautifulSoup and Requests
# Install the required packages: pip install beautifulsoup4 requests
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php' # URL of the website we want to scrape

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

# Using BeautifulSoup to parse the HTML content
import requests
from bs4 import BeautifulSoup

# Archived snapshot of the exact URL used in 30 Days of Python
url = 'https://web.archive.org/web/20220303070700/https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

# Find all tables with cellpadding='3'
tables = soup.find_all('table', {'cellpadding': '3'})

# Target the primary datasets table
table = tables[0]

# Iterate through every row and extract cell data
for tr in table.find_all('tr'):
    row_data = [td.get_text(strip=True) for td in tr.find_all('td')]
    
    # Print non-empty rows
    if row_data:
        print(row_data)