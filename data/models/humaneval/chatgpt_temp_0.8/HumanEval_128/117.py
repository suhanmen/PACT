def prod_signs(arr):
    if not arr:  # check if array is empty
        return None

    sign = 1
    magnitude_sum = 0

    for num in arr:
        if num == 0:
            sign = 0
        elif num < 0:
            sign *= -1
            magnitude_sum += abs(num)
        else:
            magnitude_sum += num

    return sign * magnitude_sum
