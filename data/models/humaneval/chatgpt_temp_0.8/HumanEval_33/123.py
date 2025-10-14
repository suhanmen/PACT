def sort_third(l: list):
    indices = range(0, len(l), 3)
    sorted_values = [l[i] for i in indices]
    sorted_values.sort()
    result = []
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(sorted_values.pop(0))
        else:
            result.append(l[i])
    return result
