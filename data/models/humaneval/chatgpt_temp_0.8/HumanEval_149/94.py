def sorted_list_sum(lst):
    # Create an empty list to store the valid strings
    valid_strings = []
    
    # Loop through the strings in the input list
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # If it is even, add it to the list of valid strings
            valid_strings.append(string)
    
    # Sort the list of valid strings first by length, then alphabetically
    valid_strings.sort(key=lambda x: (len(x), x))
    
    # Return the sorted list of valid strings
    return valid_strings
