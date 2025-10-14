def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    min_index = arr.index(min(arr))
    arr = arr[min_index:] + arr[:min_index]
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            return False
    return True
