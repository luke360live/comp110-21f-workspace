"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730288863"


"""Testing for one key/value"""


def test_invert_edge() -> None:
    first_list: dict[str, str] = {'blue': 'devils'}
    assert invert(first_list) == {'devils': 'blue'}


"""Testing for multiple keys/values"""


def test_invert_use() -> None:
    first_list: dict[str, str] = {'blue': 'devils', 'duke': 'university'}
    assert invert(first_list) == {'devils': 'blue', 'university': 'duke'}


"""Second testing for multiple keys/values"""


def test_invert_use_2() -> None:
    first_list: dict[str, str] = {'blue': 'devils', 'duke': 'university', 'go': 'team'}
    assert invert(first_list) == {'devils': 'blue', 'university': 'duke', 'team': 'go'}


"""Testing for one color."""


def test_favorite_color_edge() -> None:
    color: dict[str, str] = {"university": "blue"}
    assert favorite_color(color) == "blue"


"""Testing for multiple colors"""


def test_favorite_color_use() -> None:
    color: dict[str, str] = {"university": "blue", "Ryan": "red", "Gabe": "green"}
    assert favorite_color(color) == "blue"


"""Second testing for multiple colors"""


def test_favorite_color_use_2() -> None:
    color: dict[str, str] = {"university": "blue", "Ryan": "orange", "Gabe": "purple"}
    assert favorite_color(color) == "blue"


"""Testing for one value"""


def test_count_edge() -> None:
    first_list: list[str] = ['a']
    assert count(first_list) == {'a': 1}


"""Testing for multiple values""" 


def test_count_use() -> None: 
    first_list: list[str] = ['a', 'b', 'c']
    assert count(first_list) == {'a': 1, 'b': 2}


"""Second testing for multiple values"""


def test_count_use_2() -> None:
    first_list: list[str] = {'a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd'}
    assert count(first_list) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}