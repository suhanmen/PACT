def prod_signs(arr):
    if not arr:
        return None
    else:
        prod = 1
        mag_sum = 0
        for num in arr:
            if num == 0:
                sign = 0
            else:
                sign = num / abs(num)
            prod *= sign
            mag_sum += abs(num)
        return prod * mag_sum
