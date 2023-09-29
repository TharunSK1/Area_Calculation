import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://quotes.toscrape.com/page/1/"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and print quotes and authors
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for i in range(len(quotes)):
        print(f"Quote: {quotes[i].text}")
        print(f"Author: {authors[i].text}")
        print("-" * 50)

else:
    print("Failed to retrieve the web page.")

