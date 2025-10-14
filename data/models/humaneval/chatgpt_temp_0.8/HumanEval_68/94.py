def pluck(arr):
    even_values = []
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_values.append((val, i))
    if not even_values:
        return []
    even_values.sort()
    return [even_values[0][0], even_values[0][1]]
