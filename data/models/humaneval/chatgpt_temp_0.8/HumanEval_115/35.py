# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0
    
    num_buckets = math.ceil(total_water / bucket_capacity)
    
    heights = [0] * len(grid[0])
    for row in grid:
        for i, well in enumerate(row):
            if well == 1:
                heights[i] += 1
    
    heights.sort(reverse=True)
    
    num_lowers = 0
    while num_buckets > 0:
        for i in range(len(heights)):
            if heights[i] > 0:
                heights[i] -= 1
                num_buckets -= 1
                if num_buckets == 0:
                    break
        num_lowers += 1
    
    return num_lowers
