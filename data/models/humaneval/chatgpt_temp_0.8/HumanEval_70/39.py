def strange_sort_list(lst):
    result = []
    while lst:
        # Add minimum value to result
        min_value = min(lst)
        result.append(min_value)
        lst.remove(min_value)

        if lst:
            # Add maximum value to result
            max_value = max(lst)
            result.append(max_value)
            lst.remove(max_value)
    
    return result
