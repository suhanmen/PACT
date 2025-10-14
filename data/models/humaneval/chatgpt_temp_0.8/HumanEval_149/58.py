def sorted_list_sum(lst):
    # filter out strings with odd lengths
    filtered_lst = [word for word in lst if len(word) % 2 == 0]
    
    # sort the list by length and then alphabetically if lengths are the same
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
