def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    sorted_even = sorted(even_values)
    result = [0] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = sorted_even.pop(0)
        else:
            result[i] = l[i]
    return result
