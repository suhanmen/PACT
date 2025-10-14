def sorted_list_sum(lst):
    # Create a new list to store the even-length strings
    even_length_strings = []
    
    # Iterate through the list and append even-length strings to the new list
    for string in lst:
        if len(string) % 2 == 0:
            even_length_strings.append(string)
    
    # Sort the new list by length and then alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    return sorted_strings