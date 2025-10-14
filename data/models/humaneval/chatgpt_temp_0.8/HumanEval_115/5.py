def max_fill(grid, capacity):
    import math
    
    def get_num_buckets(bucket_capacity, num_units):
        return math.ceil(num_units / bucket_capacity)
    
    num_buckets = 0
    for row in grid:
        num_units = sum(row)
        num_buckets += get_num_buckets(capacity, num_units)
    
    return num_buckets
