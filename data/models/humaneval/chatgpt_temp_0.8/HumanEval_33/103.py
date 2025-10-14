def sort_third(l: list):
    third_indices = range(0, len(l), 3)
    third_items = [l[i] for i in third_indices]
    sorted_third_items = sorted(third_items)
    result = [l[i] if i not in third_indices else sorted_third_items.pop(0) for i in range(len(l))]
    return result
