def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        prod = 1
        sum_magnitudes = 0
        for num in arr:
            if num > 0:
                prod *= 1
                sum_magnitudes += num
            elif num < 0:
                prod *= -1
                sum_magnitudes += abs(num)
            else:
                prod *= 0
        return prod * sum_magnitudes
