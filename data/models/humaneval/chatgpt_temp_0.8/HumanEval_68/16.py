def pluck(arr):
    evens = []
    for i, node in enumerate(arr):
        if node % 2 == 0:
            evens.append((node, i))
    if not evens:
        return []
    else:
        return min(evens)
