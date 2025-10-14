def sort_third(l: list):
    # Get the sublist of values at indices that are divisible by 3
    third_indices = range(0, len(l), 3)
    third_values = [l[i] for i in third_indices]

    # Sort the third values
    sorted_third_values = sorted(third_values)

    # Create a new list with the same values as l, except at third_indices
    result = [value for i, value in enumerate(l) if i not in third_indices]

    # Insert the sorted third values at third_indices
    for i, value in zip(third_indices, sorted_third_values):
        result.insert(i, value)

    return result
