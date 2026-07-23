import streamlit as st
import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

class BookScraper(Scraper):

    def parse_data(self):
        soup = self.fetch_page()
        books=[]

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            books.append((title,price))
        return books
    
class QuoteScraper(Scraper):
    
    def parse_data(self):
        soup = self.fetch_page()
        quotes=[]

        for quote in soup.find_all("div", class_="quote"):
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            quotes.append((text,author))

        return quotes
st.title("📚WEB SCRAPER USING OOP📚")    
option=st.selectbox("choose what to scrape",("books","quotes"))

if st.button("Scrape"):

    if option == "books":
        scraper = BookScraper("https://books.toscrape.com/")
        books = scraper.parse_data()

        st.subheader("Books")
        for title, price in books:
            st.write(f"*Title:* {title}")
            st.write(f"*Price:* {price}")
            st.write("---")

    elif option == "quotes":
        scraper = QuoteScraper("https://quotes.toscrape.com/")
        quotes = scraper.parse_data()

        st.subheader("Quotes")
        for text, author in quotes:
            st.write(f"*Quote:* {text}")
            st.write(f"*Author:* {author}")
            st.write("---")