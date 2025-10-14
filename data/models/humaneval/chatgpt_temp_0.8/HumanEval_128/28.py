def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        sign = 1
        mag_sum = 0
        for num in arr:
            if num == 0:
                sign = 0
            elif num < 0:
                sign *= -1
            mag_sum += abs(num)
        return sign * mag_sum
