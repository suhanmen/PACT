def sorted_list_sum(lst):
    # Create an empty list to store even-length strings
    even_length_lst = []
    
    # Iterate through each string in the input list
    for word in lst:
        # Check if the length of the string is even
        if len(word) % 2 == 0:
            # Append the even-length string to the list
            even_length_lst.append(word)
    
    # Sort the even-length list by length and then alphabetically
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
