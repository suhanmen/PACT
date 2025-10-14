# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    wells_filled = sum(sum(row) for row in grid)
    buckets_needed = math.ceil(wells_filled / bucket_capacity)
    
    return buckets_needed
