def sort_even(l: list):
    even_values = sorted([l[i] for i in range(0, len(l), 2)])
    result = [l[i] if i % 2 != 0 else even_values.pop(0) for i in range(len(l))]
    return result
