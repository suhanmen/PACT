def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    sorted_even_values = sorted(even_values)
    result = l.copy()
    for i, value in enumerate(sorted_even_values):
        result[even_indices[i]] = value
    return result
