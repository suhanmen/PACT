def max_fill(grid, capacity):
    import math
    
    num_buckets = 0
    for row in grid:
        num_buckets += math.ceil(sum(row)/capacity) # calculate the number of buckets needed for each row and add it to the total
    
    return num_buckets
