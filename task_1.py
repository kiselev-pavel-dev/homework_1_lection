def domain_name(url: str) -> str:
    """Возвращает домен из url."""
    # Сделал без urllib библиотеки, т.к не понятно можно ли ее использовать
    # C urllib тоже могу сделать
    temp_url_list = url.split('.')
    if 'www' not in temp_url_list[0]:  # Если url без www
        return temp_url_list[0].split('/')[2]
    else:
        return temp_url_list[1]


def tests():
    """Тесты для проверки."""
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("https://www.youtube.com/") == "youtube"


if __name__ == '__main__':
    tests()
