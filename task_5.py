def count_find_num(primesL: list, limit: int) -> list:
    """Нахождение чисел, которые можно разложить на множетели из primesL."""
    result = []
    compose = 1
    for prime in primesL:
        compose *= prime
    if compose > limit:
        return []
    result.append(compose)
    for prime in primesL:
        for composition in result:
            temp = composition * prime
            while temp <= limit and temp not in result:
                result.append(temp)
                temp *= prime
    return [len(result), max(result)]


def tests():
    """Тесты для проверки."""
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []


if __name__ == '__main__':
    tests()
