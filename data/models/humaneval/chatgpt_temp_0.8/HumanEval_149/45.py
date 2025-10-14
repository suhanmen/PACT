def sorted_list_sum(lst):
    # create a new list to hold the even-length strings
    even_length_strings = []
    
    # loop through the list of strings
    for string in lst:
        # check if the length of the string is even
        if len(string) % 2 == 0:
            # if it's even, add it to the new list
            even_length_strings.append(string)
    
    # sort the new list by length and then alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    return sorted_strings
