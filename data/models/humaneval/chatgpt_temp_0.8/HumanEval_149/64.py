def sorted_list_sum(lst):
    # Create a new list to store the strings with even length
    even_length_strings = []
    
    # Iterate over each string in the input list
    for string in lst:
        # If the length of the string is even, add it to the new list
        if len(string) % 2 == 0:
            even_length_strings.append(string)
    
    # Sort the new list first by length, then alphabetically
    even_length_strings.sort(key=lambda s: (len(s), s))
    
    # Return the sorted list
    return even_length_strings
