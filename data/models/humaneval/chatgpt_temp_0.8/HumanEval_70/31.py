def strange_sort_list(lst):
    # Create an empty list to store the sorted values
    sorted_lst = []
    
    # Loop until the original list is empty
    while lst:
        # Find the minimum and maximum values in the remaining list
        min_val, max_val = min(lst), max(lst)
        
        # Remove the minimum and maximum values from the original list
        lst.remove(min_val)
        lst.remove(max_val)
        
        # Add the minimum and maximum values to the sorted list
        sorted_lst.extend([min_val, max_val])
    
    # Return the sorted list
    return sorted_lst
