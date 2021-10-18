"""Unit tests for list utility functions."""


# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730288863"


# def test_only_evens() -> None:
#    test_list: list[int] = [1, 2, 3, 4, 5, 6]
#    assert only_evens(test_list) == [2, 4, 6]

# def test_only_evens_all_evens() -> None:
#   test_list: list[int] = [2, 2, 2, 2, 2, 2]
#    assert only_evens(test_list) == [2, 2, 2, 2, 2, 2]
    
def test_only_evens() -> None:
    test_list: list[int] = []
    assert only_evens(test_list) == []

 def test_sub_empty_range() -> None:
   test_list: list[int] = []
   integer1: int = 1
   integer2: int = 4
   assert sub(test_list, 1, 4) == []


def test_sub() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    integer1: int = 1
    integer2: int = 4
    assert sub(test_list) == [2, 3, 4]


def test_concat() -> None:
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [3, 4, 5]
    assert concat(test_list1, test_list2) == [1, 2, 3, 3, 4, 5]