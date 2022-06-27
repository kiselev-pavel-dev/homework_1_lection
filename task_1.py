def domain_name(url: str) -> str:
    """Возвращает домен из url."""
    if '.' not in url:
        return None
    if 'http://' in url or 'https://' in url:
        return url.split('/')[2].split('.')[-2]
    else:
        return url.split('.')[-2]


def tests():
    """Тесты для проверки."""
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "co"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("xakep.ru") == "xakep"
    assert domain_name("logs.xakep.ru") == "xakep"
    assert domain_name("logs.xakep.ru/test") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("https://www.youtube.com/") == "youtube"
    assert domain_name("https://www.logs.youtube.com/temp") == "youtube"
    assert domain_name("https://logs.youtube.com/temp") == "youtube"


if __name__ == '__main__':
    tests()
