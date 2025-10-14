def sort_even(l: list):
    even_values = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_values.pop(0))
        else:
            result.append(l[i])
    return result
