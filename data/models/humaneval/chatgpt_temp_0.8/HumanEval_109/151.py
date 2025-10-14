def move_one_ball(arr):
    if len(arr) == 0:
        return True
    
    for i in range(len(arr)):
        if arr == sorted(arr):
            return True
        arr = [arr[-1]] + arr[:-1] # right shift operation
    
    return False
