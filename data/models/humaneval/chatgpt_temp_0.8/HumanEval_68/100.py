def pluck(arr):
    even_values = []
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_values.append((val, i))
    if not even_values:
        return []
    else:
        return min(even_values, key=lambda x: (x[0], x[1]))
