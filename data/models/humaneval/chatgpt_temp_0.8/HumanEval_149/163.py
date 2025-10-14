def sorted_list_sum(lst):
    # Create an empty list to store the even-length strings
    even_length_strings = []
    
    # Loop through the strings in the input list
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # If it is even, append it to the even_length_strings list
            even_length_strings.append(string)
    
    # Sort the even_length_strings list by length and then alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    return sorted_strings
