def max_fill(grid, capacity):
    import math

    num_buckets = 0
    for i in range(len(grid[0])):
        water_height = 0
        for j in range(len(grid)):
            water_height += grid[j][i]
        num_buckets += math.ceil(water_height / capacity)
    return num_buckets
