def strange_sort_list(lst):
    result = []
    
    # Sort the list from smallest to largest
    sorted_lst = sorted(lst)
    
    # Loop through the sorted list
    while len(sorted_lst) > 0:
        # Add the smallest value to the result
        result.append(sorted_lst.pop(0))
        
        # If there are no more values, break the loop
        if len(sorted_lst) == 0:
            break
        
        # Add the largest value to the result
        result.append(sorted_lst.pop(-1))
    
    return result
