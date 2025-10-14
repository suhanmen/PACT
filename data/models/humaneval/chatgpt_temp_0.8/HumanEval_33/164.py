def sort_third(l: list):
    new_list = l.copy()
    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    for i in third_indices:
        end = min(i + 3, len(l))
        new_list[i:end] = sorted(l[i:end])
    return new_list
