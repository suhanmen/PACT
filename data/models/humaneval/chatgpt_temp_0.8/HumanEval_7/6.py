from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    
    # Initialize an empty list to store the filtered strings
    filtered_strings = []
    
    # Loop through the input strings
    for string in strings:
        
        # Check if the substring is present in the string
        if substring in string:
            
            # If the substring is present, append the string to the filtered_strings list
            filtered_strings.append(string)
    
    # Return the filtered_strings list
    return filtered_strings
