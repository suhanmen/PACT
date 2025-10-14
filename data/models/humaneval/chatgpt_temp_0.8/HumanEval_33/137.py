def sort_third(l: list):
    third_indices = range(0, len(l), 3)
    third_values = [l[i] for i in third_indices]
    sorted_third_values = sorted(third_values)
    result = l.copy()
    for i in third_indices:
        result[i:i+3] = [sorted_third_values.pop(0)] * 3
    return result
