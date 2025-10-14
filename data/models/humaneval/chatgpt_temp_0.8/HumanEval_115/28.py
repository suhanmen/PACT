# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    total_water = sum(sum(row) for row in grid)
    buckets_needed = math.ceil(total_water / bucket_capacity)
    
    return buckets_needed
