# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    def calculate_buckets_needed(water_levels, bucket_capacity):
        total_buckets_needed = 0
        for i in range(len(water_levels)):
            buckets_needed = math.ceil(water_levels[i] / bucket_capacity)
            total_buckets_needed += buckets_needed
        return total_buckets_needed
    
    num_wells = len(grid)
    well_depths = [0] * len(grid[0])
    
    for i in range(num_wells):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                well_depths[j] += 1
    
    buckets_needed = calculate_buckets_needed(well_depths, bucket_capacity)
    return buckets_needed
