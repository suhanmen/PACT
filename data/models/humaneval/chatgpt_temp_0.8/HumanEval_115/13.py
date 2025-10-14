# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    total_water = sum(map(sum, grid))
    buckets_needed = math.ceil(total_water / bucket_capacity)
    
    return buckets_needed
