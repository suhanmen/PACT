def sort_even(l: list):
    # Get the values at the even indices
    even_values = [l[i] for i in range(len(l)) if i % 2 == 0]
    # Sort the even values
    sorted_even_values = sorted(even_values)
    # Create a new list with the sorted even values and original odd values
    result = [sorted_even_values[i//2] if i % 2 == 0 else l[i] for i in range(len(l))]
    return result
