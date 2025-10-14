def move_one_ball(arr):
    if not arr:
        return True
    
    n = len(arr)
    min_idx = arr.index(min(arr))
    
    for i in range(n):
        if arr[(i + min_idx) % n] > arr[(i + min_idx - 1) % n]:
            continue
        else:
            return False
    return True
