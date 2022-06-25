def int32_to_ip(number: int) -> str:
    """Преобразует число в ip."""
    result = []
    for i in range(3, -1, -1):
        result.append(str((number >> 8 * i) % 256))
    return '.'.join(result)


def tests():
    """Тесты для проверки."""
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"


if __name__ == '__main__':
    tests()
