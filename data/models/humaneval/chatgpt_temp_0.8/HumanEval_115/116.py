def max_fill(grid, capacity):
    import math
    
    num_buckets = 0 # counter for number of times the buckets are lowered
    
    wells = [sum(row) for row in grid] # number of units of water in each well
    
    while sum(wells) > 0:
        water_extracted = 0 # counter for amount of water extracted in each bucket
        
        for i in range(len(wells)):
            if wells[i] > 0:
                water_extracted += min(capacity, wells[i])
                wells[i] -= min(capacity, wells[i])
        
        num_buckets += 1
        
    return num_buckets
