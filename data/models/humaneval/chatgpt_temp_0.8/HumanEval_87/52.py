def get_row(lst, x):
    positions = []
    for i, sublist in enumerate(lst):
        if x in sublist:
            for j, num in sorted(enumerate(sublist), key=lambda x: x[1], reverse=True):
                if num == x:
                    positions.append((i, j))
    return positions
