# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # calculate total amount of water in the wells
    total_water = sum(sum(row) for row in grid)
    
    # if there is no water, return 0
    if total_water == 0:
        return 0
    
    # calculate the number of times we need to lower the buckets
    num_buckets = math.ceil(total_water / bucket_capacity)
    
    return num_buckets
