import math


def zeros(n: int) -> int:
    """Возвращаем количество конечных нулей в факториале n!."""
    if n <= 0:
        return 0
    k_max = int(math.log(n, 5)) + 1
    result = 0
    for i in range(1, k_max):
        result += n // (5**i)
    return result


def tests():
    """Тесты для проверки."""
    assert zeros(0) == 0
    assert zeros(1) == 0
    assert zeros(-1) == 0
    assert zeros(100) == 24
    assert zeros(6) == 1
    assert zeros(12) == 2
    assert zeros(30) == 7
    assert zeros(16) == 3
    assert zeros(1000) == 249


if __name__ == '__main__':
    tests()
