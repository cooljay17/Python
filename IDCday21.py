# Scrape headlines from a news site
import requests
from bs4 import BeautifulSoup

# Requesting the website
url = 'https://www.thehindu.com/news/national/top-news-of-the-day-centre-notifies-dates-for-2027-census-search-operations-continue-at-site-of-collapsed-iron-bridge-in-pune-and-more/article69701013.ece'
response = requests.get(url)
print("Response Code is:", response.status_code)

if response.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Finding the headlines
    headlines = soup.find_all('h4')
    # Printing the headlines
    for headline in headlines:
        print(headline.text.strip())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
