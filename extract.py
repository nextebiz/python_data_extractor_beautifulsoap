from bs4 import BeautifulSoup
import requests
import pandas as pd

books = []
weburl = "https://books.toscrape.com/catalogue/page-1.html"
get_html = requests.get(weburl)
soup = BeautifulSoup(get_html.text, "html.parser")

book_tags = soup.find_all("li", attrs={"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

for book_data in book_tags:
    book = {}
    book["title"] = book_data.find("h3").find("a").attrs["title"]
    book["price"] = book_data.find("p", class_="price_color").text[2:]
    book["stock"] = book_data.find("p", class_="instock availability").text.strip()
    book["image"] = "https://books.toscrape.com/" + book_data.find("img").attrs[
        "src"
    ].replace("../", "")
    books.append(book)

pf = pd.DataFrame(books)
pf.to_csv("myfile.csv")
