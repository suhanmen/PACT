def sorted_list_sum(lst):
    # create an empty list to store the even-length strings
    even_length_strings = []
    
    # iterate over each string in the input list
    for s in lst:
        # check if the string has an even length
        if len(s) % 2 == 0:
            # if it does, add it to the even_length_strings list
            even_length_strings.append(s)
    
    # sort the even_length_strings list first by length, then alphabetically
    sorted_list = sorted(even_length_strings, key=lambda s: (len(s), s))
    
    return sorted_list
