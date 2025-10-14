def sorted_list_sum(lst):
    # Create an empty list to store the even length strings
    even_length_lst = []
    
    # Iterate through the list and only keep the even length strings
    for word in lst:
        if len(word) % 2 == 0:
            even_length_lst.append(word)
    
    # Sort the even length list by length and then alphabetically
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
