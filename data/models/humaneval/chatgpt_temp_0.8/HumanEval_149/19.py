def sorted_list_sum(lst):
    # create a new list to store strings with even length
    even_length_lst = []
    
    # loop through the input list and add strings with even length to the new list
    for word in lst:
        if len(word) % 2 == 0:
            even_length_lst.append(word)
    
    # sort the even length list first by length, then alphabetically
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
