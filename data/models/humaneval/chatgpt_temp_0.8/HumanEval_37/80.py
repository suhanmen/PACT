def sort_even(l: list):
    even_vals = sorted([val for val in l[::2]])
    l_sorted = [even_vals.pop(0) if idx % 2 == 0 else val for idx, val in enumerate(l)]
    return l_sorted
