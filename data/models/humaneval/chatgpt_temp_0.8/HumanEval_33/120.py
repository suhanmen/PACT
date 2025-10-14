python
def sort_third(l: list):
    third_indices = range(0, len(l), 3)
    sorted_third = sorted(l[i] for i in third_indices)
    result = [x for i, x in enumerate(l) if i not in third_indices]
    for i in third_indices:
        result.insert(i, sorted_third[i // 3])
    return result
