def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    even_values_sorted = sorted(even_values)
    l_sorted = [even_values_sorted[i//2] if i % 2 == 0 else l[i] for i in range(len(l))]
    return l_sorted
