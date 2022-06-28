from itertools import combinations


def tuple_to_str(tup: tuple, s: str, search_s: str) -> str:
    """Делаем необходимую нам строку с '-' из кортежа."""
    """Если строка не подходит, возвращаем None."""
    result = ''
    j = 0
    for i in range(len(s)):
        if i in tup:
            if s[i] != search_s[j]:
                return None
            result += s[i]
            j += 1
        else:
            result += '-'
    return result


def bananas(s: str) -> set:
    """Возвращаем количество подстрок в строке s."""
    result = set()
    search_s = 'banana'
    if len(s) < len(search_s):
        return set()
    for item in combinations(range(len(s)), len(search_s)):
        temp = tuple_to_str(item, s, search_s)
        if temp:
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
