def move_one_ball(arr):
    if len(arr) <= 1:
        return True
    
    for i in range(len(arr)):
        if arr[i] > arr[(i+1)%len(arr)]:
            return False
    
    return True
