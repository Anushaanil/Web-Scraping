import requests
from bs4 import BeautifulSoup

price_selector = ".price_color"
Title_selector = ".product_pod h3 a"
rating_selector = ".star-rating"

def get_rating(tag):
    for key,rating in rating_mapper.items():
        if key in tag["class"]:
            return rating
rating_mapper = {
    "One": "✭",
    "Two": "✭✭",
    "Three": "✭✭✭",
    "Four": "✭✭✭✭",
    "Five": "✭✭✭✭✭"
}
data = requests.get("http://books.toscrape.com/").content
soup = BeautifulSoup(data, "html.parser")

prices = soup.select(price_selector)
titles = soup.select(Title_selector)
ratings = soup.select(rating_selector)

with open("book_scrape_data.csv","w",encoding="UTF-8") as book_data:
    for price, title, star in zip(prices, titles, ratings):
        book_data.write(f"{title['title']}, {price.string},{get_rating(star)}\n")

