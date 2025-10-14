def sort_third(l: list):
    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    third_values = [l[i] for i in third_indices]
    sorted_third_values = sorted(third_values)
    sorted_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_l.append(sorted_third_values.pop(0))
        else:
            sorted_l.append(l[i])
    return sorted_l
