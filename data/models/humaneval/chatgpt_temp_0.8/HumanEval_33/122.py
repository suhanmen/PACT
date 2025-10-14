def sort_third(l: list):
    new_list = l.copy()
    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    third_values = [l[i] for i in third_indices]
    sorted_third_values = sorted(third_values)
    for i in third_indices:
        new_list[i] = sorted_third_values[third_indices.index(i)]
    return new_list
