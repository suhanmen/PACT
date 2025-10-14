def max_fill(grid, capacity):
    import math
    
    num_buckets = 0
    for i in range(len(grid[0])):
        water_count = 0
        for j in range(len(grid)):
            water_count += grid[j][i]
        num_buckets += math.ceil(water_count/capacity)
    
    return num_buckets
