def max_fill(grid, capacity):
    import math
    
    # Function to get the total number of units of water in the grid
    def get_total_water(grid):
        return sum(sum(row) for row in grid)
    
    # Function to get the maximum number of units of water that can be extracted
    def get_max_water_extracted(grid, capacity):
        max_water_extracted = 0
        for row in grid:
            water_in_row = sum(row)
            if water_in_row > capacity:
                return -1
            max_water_extracted += math.ceil(water_in_row / capacity)
        return max_water_extracted
    
    total_water = get_total_water(grid)
    max_water_extracted = get_max_water_extracted(grid, capacity)
    
    # If there is no water in the grid or the buckets can extract all the water, return 0
    if total_water == 0 or max_water_extracted == -1:
        return 0
    
    # Otherwise, return the number of times you need to lower the buckets
    return math.ceil(total_water / (capacity * max_water_extracted))
