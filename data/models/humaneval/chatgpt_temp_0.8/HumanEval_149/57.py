def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the list by length, and then alphabetically if necessary
    lst = sorted(lst, key=lambda x: (len(x), x))
    
    return lst
