# CANNOT PARSE CODE SNIPPET
python
def max_fill(grid, bucket_capacity):
    import math
    
    total_water = sum(sum(row) for row in grid)
    bucket_count = math.ceil(total_water / bucket_capacity)
    return bucket_count
