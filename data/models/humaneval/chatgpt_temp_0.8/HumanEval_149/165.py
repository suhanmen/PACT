def sorted_list_sum(lst):
    # Filter out strings with odd length
    filtered_lst = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list by length and then alphabetically if lengths are equal
    filtered_lst.sort(key=lambda s: (len(s), s))
    
    return filtered_lst
