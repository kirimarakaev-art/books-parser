from dataclasses import dataclass

@dataclass
class Book:
    title: str
    price: float
    rating: int
    in_stock: bool
    url: str