# CANNOT PARSE
def move_one_ball(arr):
    if not arr:
        return True

    n = len(arr)
    count = 0

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            count += 1
            index = i

    if count > 1:
        return False

    if count == 0:
        return True

    if index == n - 2 and arr[-1] <= arr[0]:
        return True

    if index == 0 and arr[-1] <= arr[1]:
        return True

    if 0 < index < n - 2 and arr[index - 1] <= arr[index + 1] and arr[index] <= arr[index + 2]:
        return True

    return False