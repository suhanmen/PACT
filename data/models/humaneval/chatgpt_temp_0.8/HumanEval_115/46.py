# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # count the total number of water units in the wells
    total_water = sum([sum(row) for row in grid])
    
    # calculate the total number of buckets required to empty the wells
    num_buckets = math.ceil(total_water / bucket_capacity)
    
    # return the number of times the buckets need to be lowered
    return num_buckets
