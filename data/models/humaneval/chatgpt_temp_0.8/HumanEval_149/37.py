def sorted_list_sum(lst):
    # Create an empty list to store even-length strings
    even_lst = []
  
    # Loop through the input list
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # If the length is even, add it to the even_lst
            even_lst.append(word)
    
    # Sort the even_lst by length and then alphabetically
    sorted_lst = sorted(even_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
