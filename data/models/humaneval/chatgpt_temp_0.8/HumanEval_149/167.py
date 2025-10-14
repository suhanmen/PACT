def sorted_list_sum(lst):
    # Create an empty list to hold the even-length strings
    even_length_strings = []
    
    # Iterate through each string in the list
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # Append the string to the even_length_strings list
            even_length_strings.append(string)
    
    # Sort the even_length_strings list by length and then alphabetically
    even_length_strings.sort(key=lambda x: (len(x), x))
    
    # Return the sorted list of even length strings
    return even_length_strings
