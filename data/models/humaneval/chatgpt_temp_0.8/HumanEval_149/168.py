def sorted_list_sum(lst):
    # create a new list to store even length strings
    even_length_words = []
    
    # loop over each string in the list
    for string in lst:
        # check if the length of the string is even
        if len(string) % 2 == 0:
            # add the string to the new list
            even_length_words.append(string)
    
    # sort the list by length first, then alphabetically
    sorted_list = sorted(even_length_words, key=lambda x: (len(x), x))
    
    # return the sorted list
    return sorted_list
