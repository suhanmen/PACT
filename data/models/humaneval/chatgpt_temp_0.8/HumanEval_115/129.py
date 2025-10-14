# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # Count the number of units of water in each well
    well_counts = [sum(row) for row in grid]
    
    # Find the maximum number of units of water in any well
    max_water = max(well_counts)
    
    # Calculate the number of times the buckets need to be lowered
    num_buckets = math.ceil(max_water / bucket_capacity)
    
    return num_buckets
