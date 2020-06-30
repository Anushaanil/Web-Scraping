import requests
from bs4 import BeautifulSoup

c = requests.get("http://books.toscrape.com/").content
soup = BeautifulSoup(c,"html.parser")

details = soup.select("div.side_categories li a")    # ul.nav.nav-list

with open("book_scrape_data.csv","a") as f:
    for s in details:                                    # 
        f.write(s.string)