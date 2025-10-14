def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    sorted_even_values = sorted(even_values)
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 1:
            result[i] = l[i]
        else:
            result[i] = sorted_even_values.pop(0)
    return result
