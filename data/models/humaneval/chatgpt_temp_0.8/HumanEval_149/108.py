def sorted_list_sum(lst):
    # filter out strings with odd lengths
    filtered_lst = [s for s in lst if len(s) % 2 == 0]
    
    # sort the list by ascending length and alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda s: (len(s), s))
    
    return sorted_lst
