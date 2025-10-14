def sorted_list_sum(lst):
    # Create a new list to store the even length strings
    even_length = []
    
    # Iterate through the list and add even length strings
    for word in lst:
        if len(word) % 2 == 0:
            even_length.append(word)
    
    # Sort the list by length and then alphabetically
    sorted_list = sorted(even_length, key=lambda x: (len(x), x))
    
    return sorted_list
