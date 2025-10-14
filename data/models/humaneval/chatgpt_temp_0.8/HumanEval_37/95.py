def sort_even(l: list):
    even_vals = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    sorted_l = []
    for i in range(len(l)):
        if i % 2 == 0:
            sorted_l.append(even_vals.pop(0))
        else:
            sorted_l.append(l[i])
    return sorted_l
