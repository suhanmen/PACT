def sorted_list_sum(lst):
    # create a new list with only even-length strings
    even_length = [word for word in lst if len(word) % 2 == 0]
    
    # sort the list first by length, then alphabetically
    sorted_list = sorted(even_length, key=lambda x: (len(x), x))
    
    return sorted_list
