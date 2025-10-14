def sorted_list_sum(lst):
    # Create an empty list to store the even-length strings
    even_lst = []
    
    # Iterate over each string in the input list
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # If it is even, append it to the even_lst list
            even_lst.append(string)
    
    # Sort the even_lst list first by length, then alphabetically
    even_lst.sort(key=lambda x: (len(x), x))
    
    # Return the sorted even_lst list
    return even_lst
