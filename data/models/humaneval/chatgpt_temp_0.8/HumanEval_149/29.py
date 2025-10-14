def sorted_list_sum(lst):
    # Create a new list to store the even-length strings
    even_lst = []
    for word in lst:
        if len(word) % 2 == 0:
            even_lst.append(word)
    
    # Sort the even-length strings by length and then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
