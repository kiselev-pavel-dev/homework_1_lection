from itertools import combinations


def tuple_to_str(tup: tuple, s: str) -> str:
    """Делаем необходимую нам строку с '-' из кортежа."""
    result = ''
    for i in range(len(s)):
        if i in tup:
            result += s[i]
        else:
            result += '-'
    return result


def bananas(s: str) -> set:
    """Возвращаем количество подстрок в строке s."""
    result = set()
    search_s = 'banana'
    for item in combinations(range(len(s) + 1), len(search_s)):
        temp = tuple_to_str(item, s)
        if temp.replace('-', '') == search_s:
            result.add(temp)
    return result


def tests():
    """Тесты для проверки."""
    assert bananas("banan") == set()
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {
        "b-an--ana",
        "-banana--",
        "-b--anana",
        "b-a--nana",
        "-banan--a",
        "b-ana--na",
        "b---anana",
        "-bana--na",
        "-ba--nana",
        "b-anan--a",
        "-ban--ana",
        "b-anana--",
    }
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {
        "ban--ana",
        "ba--nana",
        "bana--na",
        "b--anana",
        "banana--",
        "banan--a",
    }


if __name__ == '__main__':
    tests()
