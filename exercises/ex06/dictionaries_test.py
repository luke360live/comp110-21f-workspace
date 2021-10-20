"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730288863"


def test_invert_edge() -> None:
    """Testing for one key/value"""
    first_list: dict[str, str] = {'blue': 'devils'}
    assert invert(first_list) == {'devils': 'blue'}


def test_invert_use() -> None:
    """Testing for multiple keys/values"""
    first_list: dict[str, str] = {'blue': 'devils', 'duke': 'university'}
    assert invert(first_list) == {'devils': 'blue', 'university': 'duke'}


def test_invert_use_2() -> None:
    """Second testing for multiple keys/values"""
    first_list: dict[str, str] = {'blue': 'devils', 'duke': 'university', 'go': 'team'}
    assert invert(first_list) == {'devils': 'blue', 'university': 'duke', 'team': 'go'}


def test_favorite_color_edge() -> None:
    """Testing for one color."""
    color: dict[str, str] = {"university": "blue"}
    assert favorite_color(color) == "blue"


def test_favorite_color_use() -> None:
    """Testing for multiple colors"""
    color: dict[str, str] = {"university": "blue", "Ryan": "red", "Gabe": "green"}
    assert favorite_color(color) == "blue"


def test_favorite_color_use_2() -> None:
    """Second testing for multiple colors"""
    color: dict[str, str] = {"university": "blue", "Ryan": "orange", "Gabe": "purple"}
    assert favorite_color(color) == "blue"


def test_count_edge() -> None:
    """Testing for one value"""
    first_list: list[str] = ['a']
    assert count(first_list) == {'a': 1}


def test_count_use() -> None: 
    """Testing for multiple values""" 
    first_list: list[str] = ['a', 'b', 'c']
    assert count(first_list) == {'a': 1, 'b': 2}


def test_count_use_2() -> None:
    """Second testing for multiple values"""
    first_list: list[str] = {'a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd'}
    assert count(first_list) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}