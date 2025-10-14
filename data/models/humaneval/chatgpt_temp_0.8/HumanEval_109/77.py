def move_one_ball(arr):
    if not arr:
        return True
    
    n = len(arr)
    min_val = min(arr)
    min_idx = arr.index(min_val)
    
    if min_idx == 0:
        return True
    
    # Right shift the array until the minimum value is at the start
    for i in range(n):
        if arr[i] == min_val:
            min_idx = i
            break
    for i in range(n):
        if arr[(min_idx + i) % n] != min_val + i:
            return False
    
    return True
