from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # if the list is empty
        return None  # return None
    max_length = len(strings[0])  # initialize max_length as length of first string
    longest_string = strings[0]  # initialize longest_string as first string
    for string in strings[1:]:  # iterate over remaining strings in the list
        length = len(string)
        if length > max_length:  # if the length of string is greater than max_length
            max_length = length  # update max_length
            longest_string = string  # update longest_string
    return longest_string
