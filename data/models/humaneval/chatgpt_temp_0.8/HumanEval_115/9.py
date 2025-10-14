def max_fill(grid, capacity):
    import math
    
    num_buckets = 0 # initialize the number of buckets needed to be lowered to 0
    
    for well in grid: # iterate through each well in the grid
        num_buckets += math.ceil(sum(well) / capacity) # add the number of buckets needed to empty the well to the total number of buckets needed
    
    return num_buckets # return the total number of buckets needed
