# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # count the total number of units of water in the grid
    water_count = sum(map(sum, grid))
    
    # calculate the number of times the buckets need to be lowered
    num_buckets = math.ceil(water_count / bucket_capacity)
    
    return num_buckets
