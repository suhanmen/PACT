def sorted_list_sum(lst):
    # create a new list with even-length strings
    even_length_lst = [word for word in lst if len(word) % 2 == 0]
    
    # sort the list by length of each word
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
