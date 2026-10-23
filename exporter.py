from openpyxl import Workbook

from models import Book

HEADERS = ["Название", "Цена (£)", "Рейтинг", "В наличии", "Ссылка"]


def save_to_excel(books: list[Book], path: str) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Книги"
    ws.append(HEADERS)
    for book in books:
        ws.append([
            book.title,
            book.price,
            book.rating,
            "да" if book.in_stock else "нет",
            book.url,
        ])
    wb.save(path)
