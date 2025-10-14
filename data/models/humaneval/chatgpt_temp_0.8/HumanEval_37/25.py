def sort_even(l: list):
    # Extract the even-indexed elements of the list and sort them
    evens = sorted(l[::2])
    # Return a new list that alternates between odd-indexed elements of l and sorted even-indexed elements
    return [l[i] if i % 2 == 1 else evens[i // 2] for i in range(len(l))]
