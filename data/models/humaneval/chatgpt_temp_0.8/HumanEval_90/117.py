def next_smallest(lst):
    # Remove duplicates from the list and sort it in ascending order
    sorted_list = sorted(set(lst))
    
    # Check if there is a second smallest element
    if len(sorted_list) < 2:
        return None
    
    # Return the second smallest element
    return sorted_list[1]
