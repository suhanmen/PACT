def max_fill(grid, capacity):
    import math
    
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0
    
    num_buckets = math.ceil(total_water / capacity)
    num_rows = len(grid)
    num_cols = len(grid[0])
    row_order = list(range(num_rows))
    col_order = list(range(num_cols))
    num_lowerings = 0
    
    while num_buckets > 0:
        max_well = -1
        max_well_volume = -1
        for i in row_order:
            for j in col_order:
                if grid[i][j] == 1:
                    well_volume = sum(grid[k][j] for k in range(num_rows))
                    if well_volume > max_well_volume:
                        max_well = i
                        max_well_volume = well_volume
        
        bucket_volume = min(capacity, max_well_volume)
        num_lowerings += bucket_volume
        num_buckets -= 1
        
        for j in col_order:
            if grid[max_well][j] == 1:
                grid[max_well][j] = 0
                bucket_volume -= 1
    
