# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # Get total amount of water in wells
    total_water = sum(sum(row) for row in grid)
    
    # Calculate number of bucket fills required to empty the wells
    num_fills = math.ceil(total_water / bucket_capacity)
    
    return num_fills
