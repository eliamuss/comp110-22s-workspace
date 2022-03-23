"""Testing for dictionary functions."""

__author__ = "730411607"

from exercises.ex06.dictionary import colored, inverted, count


def test_inversion_one() -> None:
    """Testing if a singular inversion is performed."""
    dictionary_b: dict[str, str] = ({'jeff': 'eliam'})
    assert inverted(dictionary_b) == {'eliam': 'jeff'} 


def test_inversion_two() -> None:
    """Testing if a multiple item inversion is performed."""
    dictionary_b: dict[str, str] = ({'egg': 'bacon', 'drink': 'water', 'brownie': 'cookie'})
    assert inverted(dictionary_b) == {'bacon': 'egg', 'water': 'drink', 'cookie': 'brownie'} 


def test_inversion_three() -> None:
    """Testing if a empty inversion is performed."""
    dictionary_b: dict[str, str] = ({})
    assert inverted(dictionary_b) == {}   


def test_color_one() -> None:
    """Testing if a singular color test is performed."""
    names_1: dict[str, str] = ({"Eliam": "green"})
    assert colored(names_1) == 'green'


def test_color_two() -> None:
    """Testing if when multiple items are used if the function is performed."""
    names_1: dict[str, str] = ({"Nebiat": "yellow", "Mussie": "black", "Lulu": "yellow", "Yoel": "green"})
    assert colored(names_1) == 'yellow'


def test_color_three() -> None:
    """Testing if an empty color is performed."""
    names_1: dict[str, str] = {}
    assert colored(names_1) == ''


def test_count_one() -> None:
    """Testing if a one instance of each word count is performed."""
    counting: list[str] = ["Bagels", "are", "morning", "sandwhiches"]
    assert count(counting) == {"Bagels": 1, "are": 1, "morning": 1, "sandwhiches": 1}


def test_count_two() -> None:
    """Testing if a repeating word count is performed."""
    counting: list[str] = ["cat", "hamster", "snake", "snake"]
    assert count(counting) == {"cat": 1, "hamster": 1, "snake": 2}


def test_count_three() -> None:
    """Testing if a empty count is performed."""
    counting: list[str] = []
    assert count(counting) == {}
