import re


def domain_name(url: str) -> str:
    """Возвращает домен из url."""
    match = re.search(
        r'((https?://)?(www.)?([A-Za-z0-9-]+).([A-Za-z]*))', url, re.I
    )
    return match.group(4)


def tests():
    """Тесты для проверки."""
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("https://www.youtube.com/") == "youtube"
    assert domain_name("https://www.youtube.com/temp") == "youtube"


if __name__ == '__main__':
    tests()
