def max_fill(grid, capacity):
    import math
    
    num_buckets = 0
    
    # Check if the grid is empty
    if not grid:
        return num_buckets
    
    # Iterate through each column and find the amount of water in each well
    for c in range(len(grid[0])):
        water_level = 0
        
        # Iterate through each row and add the water level in the current well
        for r in range(len(grid)):
            if grid[r][c] == 1:
                water_level += 1
        
        # Calculate the number of buckets needed to empty the well
        num_buckets += math.ceil(water_level / capacity)
        
    return num_buckets
