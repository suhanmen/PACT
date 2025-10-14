def sorted_list_sum(lst):
    # Convert the list to a set to remove duplicates
    lst = set(lst)
    
    # Create a new list to store the filtered strings
    filtered_lst = []
    
    # Iterate over the original list to filter out odd length strings
    for string in lst:
        if len(string) % 2 == 0:  # Check if the length is even
            filtered_lst.append(string)
    
    # Sort the filtered list by length first, then alphabetically if lengths are equal
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
