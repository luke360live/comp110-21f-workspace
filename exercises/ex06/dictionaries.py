"""Practice with dictionaries."""

__author__ = "730288863"

# Define your functions below


def invert(first_list: dict[str, str]) -> dict[str, str]:
    """Invert Function"""
    invert_dict: dict[str, str] = {}
    for key in first_list: 
        if first_list[key] in invert_dict:
            raise KeyError("Keys cannot be identical.")
        invert_dict[first_list[key]] = key
    return invert_dict


def favorite_color(color: dict[str, str]) -> str:
    """Function returning most frequent color."""
    max: int = 0
    most_popular: str = ""
    new_dict: dict[str, int] = {}
    for name in color:
        new_dict[color[name]] = 1
    for name in color:
        if color[name] in new_dict:
            new_dict[color[name]] += 1
    for name in new_dict:
        if new_dict[name] > max:
            max = new_dict[name]
            most_popular = name
    return most_popular


def count(first_list: list[str]) -> dict[str, int]:
    """Function counting frequency of integers"""
    frequency: dict[str, int] = {}
    for value in first_list:
        frequency[value] = 0
    for value in first_list:
        if value in frequency:
            frequency[value] += 1
    return frequency