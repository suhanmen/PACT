def sorted_list_sum(lst):
    # Create a new list to store the filtered strings
    filtered_lst = []
    # Iterate through the original list
    for word in lst:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # If it is even, add it to the filtered list
            filtered_lst.append(word)
    # Sort the filtered list based on length and then alphabetically
    filtered_lst.sort(key=lambda x: (len(x), x))
    # Return the filtered and sorted list
    return filtered_lst
