"""Practicing with dictionary functions."""

__author__ = "730411607"


def inverted(dictionary_a: dict[str, str]) -> dict[str, str]:
    dictionary_b: dict[str, str] = {}
    for key in dictionary_a:
        if dictionary_a[key] in dictionary_b:
            raise KeyError
        else:
            dictionary_b[dictionary_a[key]] = key
    return dictionary_b


def colored(names: dict[str, str]) -> str:
    """Goes throuhg and finds the most frequent value in a dictionary is most common."""
    new_dict: dict[str, int] = {}
    set_score: int = 0
    returning_number: str = ""
    
    for key in names:
        if names[key] in new_dict:
            new_dict[names[key]] += 1
        else:
            new_dict[names[key]] = 1
    
    for key in new_dict:
        if new_dict[key] > set_score:
            set_score = new_dict[key]
            returning_number = key
    
    return returning_number


def count(initial_list: list[str]) -> dict[str, int]:
    """Count of the number of times that value appeared in the input list."""
    return_type: dict[str, int] = dict()
    i = 0
    for item in initial_list:
        if initial_list[1] in return_type:
            return_type[initial_list[i]] += 1
        else:
            return_type[initial_list[i]] = 1
        i += 1
    return return_type
