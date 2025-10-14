def sorted_list_sum(lst):
    # create a new list to store the even-length strings
    even_lst = []
    for word in lst:
        if len(word) % 2 == 0:
            # if the length is even, add it to the new list
            even_lst.append(word)
    
    # sort the new list first by length, then alphabetically
    even_lst.sort(key=lambda x: (len(x), x))
    
    return even_lst
