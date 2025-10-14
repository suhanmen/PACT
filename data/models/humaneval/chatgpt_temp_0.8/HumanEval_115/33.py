def max_fill(grid, capacity):
    import math
    num_buckets = 0
    for row in grid:
        count = sum(row)
        num_buckets += math.ceil(count/capacity)
    return num_buckets
