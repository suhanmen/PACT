def sorted_list_sum(lst):
    # create a new list to store even-length strings
    even_length = []
    
    # iterate through each string in the list
    for word in lst:
        # if the length of the string is even
        if len(word) % 2 == 0:
            # append it to the new list
            even_length.append(word)
    
    # sort the new list first by length, then by alphabetical order
    sorted_list = sorted(even_length, key=lambda x: (len(x), x))
    
    return sorted_list
