from urllib.parse import urljoin

from bs4 import BeautifulSoup

from models import Book

RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_books(html: str, page_url: str) -> list[Book]:
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for card in soup.select("article.product_pod"):
        link = card.select_one("h3 a")
        price_text = card.select_one("p.price_color").text
        rating_classes = card.select_one("p.star-rating")["class"]
        availability = card.select_one("p.availability").text

        books.append(Book(
            title=link["title"],
            price=float(price_text.replace("£", "")),
            rating=RATINGS[rating_classes[1]],
            in_stock="In stock" in availability,
            url=urljoin(page_url, link["href"]),
        ))
    return books


def find_next_page(html: str, page_url: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")
    if next_link is None:
        return None
    return urljoin(page_url, next_link["href"])
