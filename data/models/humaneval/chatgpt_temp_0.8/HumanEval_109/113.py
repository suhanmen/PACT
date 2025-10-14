def move_one_ball(arr):
    if len(arr) < 2:
        return True

    prev = arr[0]
    shift_count = 0

    for i in range(1, len(arr)):
        if prev > arr[i]:
            shift_count += 1
            if shift_count > 1:
                return False
            prev = arr[i]
        else:
            prev = arr[i]

    return True
