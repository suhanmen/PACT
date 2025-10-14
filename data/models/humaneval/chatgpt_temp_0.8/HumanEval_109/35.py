def move_one_ball(arr):
    if len(arr) <= 1:
        return True
    
    min_index = arr.index(min(arr))
    
    for i in range(1, len(arr)):
        if arr[(min_index+i)%len(arr)] < arr[(min_index+i-1)%len(arr)]:
            return False
    
    return True
