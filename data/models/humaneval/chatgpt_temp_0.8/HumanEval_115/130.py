# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # find the total amount of water in the wells
    water = sum(sum(row) for row in grid)
    
    # calculate the number of times the buckets need to be lowered
    num_buckets = math.ceil(water / bucket_capacity)
    
    return num_buckets
