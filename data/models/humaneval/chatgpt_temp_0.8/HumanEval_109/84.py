def move_one_ball(arr):
    if not arr:
        return True
    
    min_index = arr.index(min(arr))
    
    for i in range(len(arr)):
        if arr[(i + min_index) % len(arr)] > arr[(i + min_index + 1) % len(arr)]:
            return False
        
    return True
