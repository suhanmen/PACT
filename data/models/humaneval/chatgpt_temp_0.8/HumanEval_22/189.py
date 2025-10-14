from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Create an empty list to store the filtered integers
    filtered_integers = []
    
    # Loop through the input list
    for value in values:
        # Check if the value is an integer
        if isinstance(value, int):
            filtered_integers.append(value)
    
    return filtered_integers
