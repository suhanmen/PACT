def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = sorted([l[i] for i in even_indices])
    sorted_l = l[:]
    for i in even_indices:
        sorted_l[i] = even_values.pop(0)
    return sorted_l
