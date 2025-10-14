def sorted_list_sum(lst):
    # Create a new list to hold only the strings with even lengths
    even_length_lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the even-length list first by length, then alphabetically
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
