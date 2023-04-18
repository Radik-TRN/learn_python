def test_greeting(name, age):
    greeting = f'Привет, {name}! Тебе {age} лет.'

    print(greeting)
    assert greeting == "Привет, Анна! Тебе 25 лет."

test_greeting("Анна", 25)


def test_rectangle(length: int, width: int):
    perimeter = (length + width) * 2

    print(perimeter)
    assert perimeter == 60

    area = length * width

    print(area)
    assert area == 200

test_rectangle(10, 20)


def test_circle(radius):
    pi = 3.14
    area = pi * radius**2

    print(area)
    assert area == 1661.0600000000002

    length = 2 * pi * radius

    print(length)
    assert length == 144.44

test_circle(23)


def test_random_list(numbers: list):

    print(len(numbers))
    assert len(numbers) == 10

    print(sorted(numbers))
    assert sorted(numbers)
    assert numbers[0] < numbers[-1]

test_random_list([1, 9, 7, 4, 2, 0, 3, 6, 8, 11])


def test_unique_elements(numbers: list):

    numbers_new = list(set(numbers))
    print(numbers_new)

    assert isinstance(numbers_new, list)
    assert len(numbers_new) == 10
    assert numbers_new == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test_unique_elements([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10])


def test_dicts(first: list, second: list):
    dict_new = dict(zip(first, second))
    print(dict_new)

    assert isinstance(dict_new, dict)
    assert len(dict_new) == 5

test_dicts(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])

