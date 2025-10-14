def max_fill(grid, capacity):
    import math
    
    def get_total_water(grid):
        return sum(sum(row) for row in grid)

    def can_empty(grid, level, capacity):
        num_buckets = 0
        for row in grid:
            if sum(row) > level:
                num_buckets += math.ceil((sum(row) - level) / capacity)
        return num_buckets <= level
    
    if not grid or not grid[0]:
        return 0
    
    total_water = get_total_water(grid)
    if total_water == 0:
        return 0
    
    low, high = 0, total_water
    while low < high:
        mid = (low + high) // 2
        if can_empty(grid, mid, capacity):
            high = mid
        else:
            low = mid + 1
    
    return low
