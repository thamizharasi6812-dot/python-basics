from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
import json
import csv

class Scraper(ABC):
    total_scrapers = 0

    def __init__(self, url):
        self.__url = url
        self.data = []
        Scraper.total_scrapers += 1

    @property
    def url(self):
        return self.__url

    def fetch_page(self):
        response = requests.get(self.__url)
        return BeautifulSoup(response.text, "html.parser")

    @abstractmethod
    def parse_data(self):
        pass

class BookScraper(Scraper):

    def parse_data(self):
        soup = self.fetch_page()

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            self.data.append({
                "Title": title,
                "Price": price
            })

        return self.data

class QuoteScraper(Scraper):

    def parse_data(self):
        soup = self.fetch_page()

        for quote in soup.find_all("div", class_="quote"):
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            self.data.append({
                "Quote": text,
                "Author": author
            })

        return self.data

class DataExporter:

    @staticmethod
    def save_json(filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_csv(filename, data):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

class ScraperManager:

    def run(self):
        print("1. Scrape Books")
        print("2. Scrape Quotes")

        choice = input("Enter your choice: ")

        if choice == "1":
            scraper = BookScraper("https://books.toscrape.com/")
            data = scraper.parse_data()

        elif choice == "2":
            scraper = QuoteScraper("https://quotes.toscrape.com/")
            data = scraper.parse_data()

        else:
            print("Invalid choice")
            return

        print("\nExtracted Data:")
        for item in data[:5]:
            print(item)

        DataExporter.save_json("output.json", data)
        DataExporter.save_csv("output.csv", data)

        print("\nData saved successfully!")
        print("Total Scrapers Created:", Scraper.total_scrapers)

manager = ScraperManager()
manager.run()