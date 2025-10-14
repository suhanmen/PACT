def move_one_ball(arr):
    if not arr:
        return True

    n = len(arr)
    min_val = min(arr)
    min_idx = arr.index(min_val)

    for i in range(n):
        idx = (min_idx + i) % n
        if arr[idx] < min_val or arr[idx] > arr[(idx+1) % n]:
            return False

    return True
