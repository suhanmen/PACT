from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    
    filtered_list = []  # initialize an empty list to store the filtered strings
    
    for string in strings:  # iterate through the input list of strings
        if substring in string:  # check if the substring is present in the current string
            filtered_list.append(string)  # add the current string to the filtered list
    
    return filtered_list  # return the filtered list of strings

