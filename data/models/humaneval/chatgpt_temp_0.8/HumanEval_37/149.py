def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    even_values_sorted = sorted(even_values)
    l_sorted = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            l_sorted[i] = even_values_sorted.pop(0)
        else:
            l_sorted[i] = l[i]
    return l_sorted
