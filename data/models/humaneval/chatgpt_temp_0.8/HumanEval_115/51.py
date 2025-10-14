# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    water_levels = [sum(row) for row in grid]
    max_level = max(water_levels)
    total_buckets = math.ceil(max_level / bucket_capacity)
    filled_buckets = 0
    
    for i in range(total_buckets):
        remaining_capacity = bucket_capacity
        for j in range(m):
            if water_levels[j] >= max_level:
                if remaining_capacity >= max_level:
                    remaining_capacity -= max_level
                    water_levels[j] = 0
                    filled_buckets += 1
                else:
                    water_levels[j] -= remaining_capacity
                    filled_buckets += 1
                    break
        max_level = max(water_levels)
    
    return filled_buckets
