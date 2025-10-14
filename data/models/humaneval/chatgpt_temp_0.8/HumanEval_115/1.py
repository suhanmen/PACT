# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # Initialize variables
    num_buckets = 0
    wells = sum(sum(row) for row in grid)
    
    # If there are no wells, return 0
    if wells == 0:
        return 0
    
    # Calculate number of buckets needed
    num_buckets = math.ceil(wells/bucket_capacity)
    
    return num_buckets
