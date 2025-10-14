def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    for i in range(n):
        if arr == sorted(arr):
            return True
        arr = [arr[-1]] + arr[:-1] # right shift operation
    return False
