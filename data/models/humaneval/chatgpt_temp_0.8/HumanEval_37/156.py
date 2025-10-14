def sort_even(l: list):
    # Extract the even-indexed elements and sort them
    even = sorted(l[::2])
    
    # Create the result list with the same length as the input list
    result = [None] * len(l)
    
    # Fill in the even-indexed elements with the sorted even elements
    result[::2] = even
    
    # Fill in the odd-indexed elements with the original values
    result[1::2] = l[1::2]
    
    return result
