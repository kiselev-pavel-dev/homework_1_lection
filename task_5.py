def prime_factors(n: int, primesL: list) -> bool:
    """Нахождение чисел, которые можно разложить на множетели из primesL."""
    i = 0
    used_numbers = set()
    while primesL[i] * primesL[i] <= n and i <= len(primesL) - 1:
        if n % primesL[i]:
            i += 1
            if i == len(primesL):
                return False
        else:
            n //= primesL[i]
            used_numbers.add(primesL[i])
    if n > 1 and n not in primesL:
        return False
    used_numbers.add(n)
    if used_numbers != set(primesL):
        return False
    return True


def count_find_num(primesL: list, limit: int) -> list:
    """Нахождение чисел, которые можно разложить на множетели из primesL."""
    count = 0
    max = 0
    for i in range(min(primesL), limit + 1):
        if prime_factors(i, primesL):
            count += 1
            max = i
    if count == 0:
        return []
    return [count, max]


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
