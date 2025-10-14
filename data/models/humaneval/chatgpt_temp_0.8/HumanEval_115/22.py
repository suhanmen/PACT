# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    total_water = 0
    for row in grid:
        total_water += sum(row)
    
    num_buckets = math.ceil(total_water / bucket_capacity)
    return num_buckets
