# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    num_buckets = 0
    
    # Iterate through each well
    for well in grid:
        # Count the number of units of water in the well
        water_count = sum(well)
        
        # Calculate the number of times the bucket needs to be lowered for this well
        num_buckets += math.ceil(water_count / bucket_capacity)
    
    return num_buckets
