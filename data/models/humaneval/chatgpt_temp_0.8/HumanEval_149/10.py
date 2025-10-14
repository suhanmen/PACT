def sorted_list_sum(lst):
    # Create a new list to store the filtered strings
    filtered_lst = []
    
    # Loop through the original list and filter out strings with odd lengths
    for word in lst:
        if len(word) % 2 == 0:
            filtered_lst.append(word)
    
    # Sort the filtered list by length and alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
