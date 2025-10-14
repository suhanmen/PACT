def sort_third(l: list):
    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    third_values = [l[i] for i in third_indices]
    sorted_third_values = sorted(third_values)
    result = l.copy()
    for i in third_indices:
        result[i] = sorted_third_values.pop(0)
    return result
