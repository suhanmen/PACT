# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # Find total amount of water in the grid
    total_water = sum([sum(row) for row in grid])
    
    # If there is no water in the grid, return 0
    if total_water == 0:
        return 0
    
    # Calculate the number of times the bucket needs to be lowered
    return math.ceil(total_water / bucket_capacity)
