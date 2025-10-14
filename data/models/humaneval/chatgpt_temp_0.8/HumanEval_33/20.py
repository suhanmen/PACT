def sort_third(l: list):
    # Create a copy of the input list
    l_ = l.copy()
    # Iterate over the indices of the list that are divisible by 3
    for i in range(0, len(l), 3):
        # Sort the values at those indices
        l_[i:i+3] = sorted(l[i:i+3])
    # Return the modified copy of the list
    return l_
