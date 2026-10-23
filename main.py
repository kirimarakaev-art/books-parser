import time

from exporter import save_to_excel
from fetcher import get_page
from parser import find_next_page, parse_books

START_URL = "https://books.toscrape.com/catalogue/page-1.html"
OUTPUT_FILE = "books.xlsx"
DELAY = 1


def main() -> None:
    all_books = []
    url = START_URL
    page = 1
    while url:
        html = get_page(url)
        books = parse_books(html, url)
        all_books.extend(books)
        print(f"Страница {page}: найдено {len(books)} книг")

        url = find_next_page(html, url)
        page += 1
        if url:
            time.sleep(DELAY)

    save_to_excel(all_books, OUTPUT_FILE)
    print(f"Готово: {len(all_books)} книг сохранено в {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
