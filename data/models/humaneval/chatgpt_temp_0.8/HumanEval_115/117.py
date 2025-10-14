# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    def num_buckets_needed(well, capacity):
        return math.ceil(sum(well)/capacity)
    
    total_buckets_needed = 0
    for well in grid:
        total_buckets_needed += num_buckets_needed(well, bucket_capacity)
        
    return total_buckets_needed
