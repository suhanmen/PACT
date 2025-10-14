def sort_third(l: list):
    # Copy the list to avoid modifying the original input
    l_prime = l.copy()
    # Create a list of indices that are divisible by three
    indices = [i for i in range(len(l)) if i % 3 == 0]
    # Sort the values at those indices
    sorted_values = sorted([l[i] for i in indices])
    # Replace the values at those indices in the copy of the list
    for i in indices:
        l_prime[i] = sorted_values.pop(0)
    return l_prime
