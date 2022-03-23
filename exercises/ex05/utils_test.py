"""EX05 - Testing for the plementation of function skeletons."""

__author__ = "730411607"

from utils import only_evens
from utils import sub
from utils import concat


def test_blank_even() -> None:
    """Testing if a blank list is returned."""
    assert only_evens([]) == [] 
    

def test_single_even_2() -> None:
    """Testing if a singular item is returned."""
    assert only_evens([10]) == [10] 
    

def test_multiple_even() -> None:
    """Testing if multiple items are returned."""
    main_list: list[int] = [4, 5, 6, 7, 8, 9, 10, 11]
    assert only_evens(main_list) == [4, 6, 8, 10] 
    

def test_empty_sub() -> None:
    """Testing if an empty sub list is returned."""
    assert sub([], 2, 3) == []
    

def test_negative_sub() -> None:
    """Testing if a negative sub list is returned."""
    assert sub([5, -2, 4, 9, 8, 23], -1, 3) == [5, -2, 4]
    

def test_use_sub() -> None:
    """Testing if a zero sub list is returned."""
    assert sub([5, -2, 4, 9, 8, 23], 1, 3) == [-2, 4]
    

def test_zero_sub() -> None:
    """Testing if a zero sub list is returned."""
    assert sub([5, -2, 4, 9, 8, 23], 0, 3) == [5, -2, 4]


def test_empty_concat() -> None:
    """Testing if an empty concat list is returned."""
    assert concat([], []) == ([]) 


def test_single_concat() -> None:
    """Testing if an empty concat list is returned."""
    assert concat([2], [10]) == ([2, 10]) 


def test_large_concat() -> None:
    """Testing if a long concat list is returned."""
    assert concat([13, 43, 345, -23, 0], [45, 12, -34, 232, 1]) == ([13, 43, 345, -23, 0, 45, 12, -34, 232, 1])