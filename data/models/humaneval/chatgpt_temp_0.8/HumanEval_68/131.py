def pluck(arr):
    even_values = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_values.append((arr[i], i))
    if len(even_values) == 0:
        return []
    else:
        min_val = even_values[0][0]
        min_index = even_values[0][1]
        for j in range(1, len(even_values)):
            if even_values[j][0] < min_val:
                min_val = even_values[j][0]
                min_index = even_values[j][1]
        return [min_val, min_index]
