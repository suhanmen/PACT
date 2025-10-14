def max_fill(grid, capacity):
    import math
    
    def count_buckets(well_heights, capacity):
        total_buckets = 0
        for well_height in well_heights:
            total_buckets += math.ceil(well_height / capacity)
        return total_buckets
    
    well_heights = [sum(row) for row in grid]
    return count_buckets(well_heights, capacity)
