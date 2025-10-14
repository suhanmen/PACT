def sorted_list_sum(lst):
    # Create a new list to store the even-length strings
    even_length_strings = []
    for string in lst:
        # Check the length of the string
        if len(string) % 2 == 0:
            # If the length is even, add it to the list
            even_length_strings.append(string)
    
    # Sort the list by length of each word and alphabetically for words with the same length
    even_length_strings.sort(key=lambda x: (len(x), x))
    
    return even_length_strings
