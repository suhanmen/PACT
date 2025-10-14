def sort_even(l: list):
    even_values = sorted([l[i] for i in range(0, len(l), 2)])
    sorted_list = []
    for i, val in enumerate(l):
        if i % 2 == 0:
            sorted_list.append(even_values.pop(0))
        else:
            sorted_list.append(val)
    return sorted_list
