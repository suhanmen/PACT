# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    def calculate_num_buckets_needed(num_water_units, bucket_capacity):
        return math.ceil(num_water_units / bucket_capacity)
    
    total_num_buckets_needed = 0
    
    for row in grid:
        num_water_units_in_row = sum(row)
        num_buckets_needed_for_row = calculate_num_buckets_needed(num_water_units_in_row, bucket_capacity)
        total_num_buckets_needed += num_buckets_needed_for_row
    
    return total_num_buckets_needed
