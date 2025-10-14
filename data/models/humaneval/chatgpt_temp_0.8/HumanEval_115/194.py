def max_fill(grid, capacity):
    import math
    
    num_buckets = 0 # initialize the count of buckets used to 0
    
    # find the total number of units of water in the grid
    total_water = sum([sum(row) for row in grid])
    
    # calculate the number of times the buckets need to be lowered
    num_buckets = math.ceil(total_water / capacity)
    
    return num_buckets
