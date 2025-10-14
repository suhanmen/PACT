def sorted_list_sum(lst):
    # Create a new list to hold the even-length strings
    even_length_strings = []
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # If it is, add it to the new list
            even_length_strings.append(word)
    # Sort the list by length, then alphabetically
    even_length_strings.sort(key=lambda x: (len(x), x))
    return even_length_strings
