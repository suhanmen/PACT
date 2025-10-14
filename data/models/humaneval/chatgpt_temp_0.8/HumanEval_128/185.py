# CANNOT PARSE
def prod_signs(arr):
    if not arr:
        return None
    else:
        product = 1
        sum_of_magnitudes = 0
        for num in arr:
            if num > 0:
                product *= 1
                sum_of_magnitudes += num
            elif num < 0:
                product *= -1
                sum_of_magnitudes += abs(num)
            else:
                product *= 0
        return product * sum_of_magnitudes
