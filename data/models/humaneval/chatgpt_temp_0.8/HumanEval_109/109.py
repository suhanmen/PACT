def move_one_ball(arr):
    if len(arr) <= 1:
        return True
    
    min_val = min(arr)
    min_idx = arr.index(min_val)
    sorted_arr = sorted(arr)
    
    for i in range(len(arr)):
        idx = (min_idx + i) % len(arr)
        if arr[idx] != sorted_arr[i]:
            return False
    
    return True
