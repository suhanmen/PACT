def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    sorted_evens = sorted([l[i] for i in even_indices])
    result = [l[i] if i % 2 != 0 else sorted_evens.pop(0) for i in range(len(l))]
    return result
