def sorted_list_sum(lst):
    # Create a new list to hold even length strings
    even_strings = []
    
    # Iterate through each string in the original list
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # If it's even, add it to the new list
            even_strings.append(string)
    
    # Sort the even_strings list first by length, then alphabetically
    even_strings.sort(key=lambda x: (len(x), x))
    
    # Return the sorted list
    return even_strings
