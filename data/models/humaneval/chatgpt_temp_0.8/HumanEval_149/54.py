def sorted_list_sum(lst):
    # Create a new list to store even-length strings
    even_length_lst = []
    
    # Iterate through the original list
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # If the length is even, add it to the new list
            even_length_lst.append(word)
            
    # Sort the new list by length and then alphabetically
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
