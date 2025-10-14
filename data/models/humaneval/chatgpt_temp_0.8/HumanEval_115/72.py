# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0
    
    num_buckets = math.ceil(total_water / bucket_capacity)
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    wells = []
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                wells.append((i, j))
    
    buckets = [(0, 0)] * num_buckets
    for i in range(num_buckets):
        buckets[i] = (wells[i][0], i % num_cols)
    
    curr_bucket = 0
    num_dips = 0
    
    while curr_bucket < num_buckets:
        row, col = buckets[curr_bucket]
        if grid[row][col] == 1:
            grid[row][col] = 0
            curr_bucket += 1
        else:
            buckets[curr_bucket] = ((row + 1) % num_rows, col)
        num_dips += 1
    
    return num_dips
