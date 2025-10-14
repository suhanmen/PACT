def sort_even(l: list):
    even_values = sorted([l[i] for i in range(0, len(l), 2)])
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = l[i]
        else:
            result[i] = even_values.pop(0)
    return result
