"""EX05 - Testing for the plementation of function skeletons."""

__author__ = "730411607"

from utils import only_evens
from utils import sub
from utils import concat


def empty_test_even() -> None:
    assert only_evens([]) == [] 
    """Testing if a blank list is returned."""


def single_test_even() -> None:
    assert only_evens([10]) == [] 
    """Testing if a singular item is returned."""


def multiple_test_even() -> None:
    main_list: list[int] = [4, 5, 6, 7, 8, 9, 10, 11]
    assert only_evens(main_list) == [] 
    """Testing if multiple items are returned."""


def empty_test_sub() -> None:
    assert sub([], 2, 3) == []
    """Testing if an empty sub list is returned."""


def negative_test_sub() -> None:
    assert sub([5, -2, 4, 9, 8, 23], -1, 3) == []
    """Testing if a negative sub list is returned."""


def zero_test_sub() -> None:
    assert sub([5, -2, 4, 9, 8, 23], 0, 3) == []
    """Testing if a zero sub list is returned."""


def empty_test_concat() -> None:
    assert concat([], []) == ([])
    """Testing if an empty concat list is returned."""


def large_test_concat() -> None:
    assert concat([13, 43, 345, -23, 0], [45, 12, -34, 232, 1]) == ([])
    """Testing if a long concat list is returned."""