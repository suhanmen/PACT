def sorted_list_sum(lst):
    # First, filter out the strings with odd lengths
    filtered_lst = [word for word in lst if len(word)%2==0]
    
    # Then, sort the filtered list by length and alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))
    
    # Finally, return the sorted list
    return sorted_lst
