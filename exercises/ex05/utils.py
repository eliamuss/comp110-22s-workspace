"""EX05 - Implementation of function skeletons."""

__author__ = "730411607"


def only_evens(main_list: list[int]) -> list[int]: 
    """Begins to define what the primary stored list will be set to."""
    even_list: list[int] = []
    i = 0 

    """Allows to go through each piece of data in the list."""
    while i < len(main_list):
        if main_list[i] % 2 == 0:
            even_list.append(main_list[i])
        i += 1
    return even_list


"""Generates a List which is a subset of the given list, between the specified start index and the end index."""


def sub(main_list: list[int], start_index: (int), end_index: (int)) -> list[int]:
    if start_index < 0:     
        start_index = 0
    if end_index > len(main_list):
        end_index == len(main_list)
    if end_index <= 0 or start_index > len(main_list):
        return []
    else:
        sub_list = []
        while start_index < len(main_list) and end_index > start_index:
            sub_list.append(main_list[start_index])
            start_index += 1
        return sub_list 


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Generates a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    blank_list: list[int] = []
    holder = first_list + second_list
    grouped_list = blank_list + holder
    return grouped_list