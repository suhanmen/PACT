def sort_third(l: list):
    # Create a list to store the sorted values at each third index
    sorted_thirds = []
    for i in range(0, len(l), 3):
        # Get the slice of the list that corresponds to this third index
        slice = l[i:i+3]
        # Sort the slice and append it to the sorted_thirds list
        sorted_slice = sorted(slice)
        sorted_thirds.append(sorted_slice)
    # Create a new list to hold the final result
    result = []
    for i, val in enumerate(l):
        # If this index is divisible by three, use the sorted value from sorted_thirds
        if i % 3 == 0:
            result.append(sorted_thirds[i//3][0])
            sorted_thirds[i//3].pop(0)
        # Otherwise, just add the original value from l
        else:
            result.append(val)
    return result
