def move_one_ball(arr):
    if not arr:
        return True
    
    n = len(arr)
    min_index = arr.index(min(arr))
    
    for i in range(n):
        if arr[(min_index+i)%n] != sorted(arr)[i]:
            return False
    return True
