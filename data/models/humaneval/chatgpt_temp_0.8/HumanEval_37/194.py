def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values_sorted = sorted([l[i] for i in even_indices])
    result = l.copy()
    for i in even_indices:
        result[i] = even_values_sorted.pop(0)
    return result
