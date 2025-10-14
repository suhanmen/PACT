def max_fill(grid, capacity):
    import math

    num_buckets = 0
    num_wells = len(grid)
    num_units = sum(sum(row) for row in grid)

    if num_units == 0:
        return 0

    num_buckets = math.ceil(num_units / capacity)

    return num_buckets
