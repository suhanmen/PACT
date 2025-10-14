def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        magnitude_sum = 0
        sign_product = 1
        for num in arr:
            if num != 0:
                magnitude_sum += abs(num)
                if num < 0:
                    sign_product *= -1
            else:
                sign_product = 0
        return magnitude_sum * sign_product
