# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    def calculate_buckets_needed(water):
        return math.ceil(water / bucket_capacity)
    
    total_buckets = 0
    for row in grid:
        water = sum(row)
        total_buckets += calculate_buckets_needed(water)
    
    return total_buckets
