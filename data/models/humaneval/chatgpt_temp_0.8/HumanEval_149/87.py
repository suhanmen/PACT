def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered_lst = list(filter(lambda x: len(x) % 2 == 0, lst))
    
    # Sort the list by length and then alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
