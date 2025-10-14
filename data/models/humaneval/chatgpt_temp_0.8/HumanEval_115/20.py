def max_fill(grid, capacity):
    import math

    total_units = 0
    for row in grid:
        total_units += sum(row)
    if total_units == 0:
        return 0

    num_buckets = int(math.ceil(total_units / capacity))
    num_lowerings = 0
    for i in range(num_buckets):
        units_extracted = 0
        for row in grid:
            for j in range(len(row)):
                if row[j] == 1:
                    row[j] = 0
                    units_extracted += 1
                    if units_extracted == capacity:
                        break
            if units_extracted == capacity:
                break
        num_lowerings += 1
    return num_lowerings
