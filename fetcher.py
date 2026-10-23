import requests


def get_page(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text
    