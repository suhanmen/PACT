def sort_even(l: list):
    even_values = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    sorted_l = [l[i] if i % 2 != 0 else even_values[i//2] for i in range(len(l))]
    return sorted_l
