def sorted_list_sum(lst):
    # Create an empty list to store the even length strings
    even_length_strings = []
    
    # Loop through the list of strings
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # If the length is even, add the string to the even_length_strings list
            even_length_strings.append(string)
    
    # Sort the list of even length strings by length and then alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda s: (len(s), s))
    
    return sorted_strings
