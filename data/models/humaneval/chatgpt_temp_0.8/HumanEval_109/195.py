def move_one_ball(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr)):
        if arr == sorted(arr):
            return True
        arr = [arr[-1]] + arr[:-1]
    return False
