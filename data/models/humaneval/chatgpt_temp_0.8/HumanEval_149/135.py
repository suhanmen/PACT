def sorted_list_sum(lst):
    # Create an empty list to hold the even-length strings
    even_lst = []
    
    # Iterate over each string in the input list
    for word in lst:
        # Check if the length of the string is even
        if len(word) % 2 == 0:
            # If the length is even, add the string to the even-length list
            even_lst.append(word)
    
    # Sort the even-length list first by length, then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    
    # Return the sorted list
    return sorted_lst
