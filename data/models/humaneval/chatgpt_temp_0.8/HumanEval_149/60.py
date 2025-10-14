def sorted_list_sum(lst):
    # Create a new list to store even-length strings
    even_lst = []
    
    # Iterate through each string in the input list
    for s in lst:
        # Check if the length of the string is even
        if len(s) % 2 == 0:
            # If the length is even, add the string to the new list
            even_lst.append(s)
    
    # Sort the new list first by length, then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
