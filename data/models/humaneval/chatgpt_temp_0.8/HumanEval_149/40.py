def sorted_list_sum(lst):
    # Create a new list to store the even-length strings
    even_len_lst = []
    
    # Loop through the original list and add the even-length strings to the new list
    for word in lst:
        if len(word) % 2 == 0:
            even_len_lst.append(word)
    
    # Sort the list by length and then alphabetically
    sorted_lst = sorted(even_len_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
