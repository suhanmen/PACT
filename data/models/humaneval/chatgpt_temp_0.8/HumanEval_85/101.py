def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices."""
    total = 0
    for i in range(1, len(lst), 2): # Loop through odd indices
        if lst[i] % 2 == 0: # Check if element at odd index is even
            total += lst[i] # Add to total if even
    return total
