# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # calculate the total amount of water in the wells
    total_water = sum(sum(row) for row in grid)
    
    # calculate the total number of buckets needed to empty the wells
    num_buckets = math.ceil(total_water / bucket_capacity)
    
    return num_buckets
