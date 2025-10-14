def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    for i in range(n):
        if arr == sorted(arr):
            return True
        arr.insert(0, arr.pop())
    return False
