def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    min_idx = arr.index(min(arr))
    for i in range(n):
        if arr[(min_idx+i)%n] != i+min(arr):
            return False
    return True
