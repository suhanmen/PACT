def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    sorted_list = [l[i] if i % 2 == 1 else even_values.pop(0) for i in range(len(l))]
    return sorted_list
