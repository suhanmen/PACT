# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # Calculate total water in wells
    total_water = sum(sum(row) for row in grid)
    
    # Calculate number of times bucket needs to be lowered
    num_lowerings = math.ceil(total_water / bucket_capacity)
    
    return num_lowerings
