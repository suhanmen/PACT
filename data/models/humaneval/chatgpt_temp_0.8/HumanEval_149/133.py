def sorted_list_sum(lst):
    # Create an empty list to store the even-length strings
    even_length = []
    
    # Iterate through the list and append even-length strings to the new list
    for word in lst:
        if len(word) % 2 == 0:
            even_length.append(word)
    
    # Sort the even-length strings first by length, then alphabetically
    even_length.sort(key=lambda x: (len(x), x))
    
    return even_length
