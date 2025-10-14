def sort_third(l: list):
    third_indices = list(range(0, len(l), 3))
    sorted_thirds = sorted([l[i] for i in third_indices])
    result = l.copy()
    for i in third_indices:
        result[i] = sorted_thirds.pop(0)
    return result
