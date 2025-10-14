def search(lst):
    # Initialize the maximum value found so far
    max_val = -1
    
    # Loop over each unique integer in the list
    for val in set(lst):
        # Compute the frequency of the current integer
        freq = lst.count(val)
        
        # Check if the current integer meets the conditions
        if val > 0 and freq >= val and val > max_val:
            # Update the maximum value found so far
            max_val = val
    
    # Return the maximum value found, or -1 if no such value exists
    return max_val
