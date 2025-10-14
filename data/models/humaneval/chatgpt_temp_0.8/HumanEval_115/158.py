def max_fill(grid, capacity):
    import math
    m = len(grid) # number of rows
    n = len(grid[0]) # number of columns
    total_water = 0 # total amount of water in the wells
    for i in range(m):
        total_water += sum(grid[i])
    # calculate the number of times the buckets need to be lowered
    num_buckets = math.ceil(total_water/capacity)
    return num_buckets
