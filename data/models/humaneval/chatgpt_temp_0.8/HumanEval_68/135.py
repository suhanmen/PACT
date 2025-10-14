def pluck(arr):
    even_values = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_values.append((arr[i], i))
    if len(even_values) == 0:
        return []
    else:
        even_values.sort()
        return [even_values[0][0], even_values[0][1]]
