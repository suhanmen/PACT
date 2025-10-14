def sort_even(l: list):
    even_values = sorted([value for index, value in enumerate(l) if index % 2 == 0])
    result = [None] * len(l)
    for index, value in enumerate(l):
        if index % 2 == 0:
            result[index] = even_values.pop(0)
        else:
            result[index] = value
    return result
