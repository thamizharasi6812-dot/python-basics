import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

class BookScraper(Scraper):

    def __init__(self,url):
       super().__init__(url)

    def parse_data(self):
        soup = self.fetch_page()

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text

            print("Title :", title)
            print("Price :", price)
            print("-" * 30)

class QuoteScraper(Scraper):
    def __init__(self,url):
       super().__init__(url)

    def parse_data(self):
        soup = self.fetch_page()

        for quote in soup.find_all("div", class_="quote"):
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            print("Quote :", text)
            print("Author:", author)
            print("-" * 30)

print("1. Scrape Books")
print("2. Scrape Quotes")

choice = input("Enter your choice: ")

if choice=="1":
 scraper =BookScraper("https://books.toscrape.com/")
 scraper.parse_data()
elif choice=="2":
 scraper =QuoteScraper("https://quotes.toscrape.com/")
 scraper.parse_data()
else:
 print("Invalid Choice")