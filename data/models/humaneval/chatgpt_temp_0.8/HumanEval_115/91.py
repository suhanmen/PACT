def max_fill(grid, capacity):
    import math
    
    total_count = 0
    
    # Calculate the total amount of water in the wells
    water_count = 0
    for row in grid:
        water_count += sum(row)
    
    # Calculate the number of buckets needed to empty all the wells
    bucket_count = math.ceil(water_count / capacity)
    
    # Iterate over the wells and empty them one by one
    for _ in range(bucket_count):
        # Iterate over each row in the grid
        for i in range(len(grid)):
            # If the row is empty, move on to the next row
            if sum(grid[i]) == 0:
                continue
            # Iterate over each well in the row
            for j in range(len(grid[i])):
                # If the well is empty, move on to the next well
                if grid[i][j] == 0:
                    continue
                # If the bucket still has space, empty the well
                if capacity > 0:
                    grid[i][j] = 0
                    capacity -= 1
                    wa
