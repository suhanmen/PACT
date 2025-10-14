def prod_signs(arr):
    if not arr:
        return None

    sign_product = 1
    magnitudes_sum = 0
    for num in arr:
        sign_product *= 1 if num > 0 else -1 if num < 0 else 0
        magnitudes_sum += abs(num)
    
    return sign_product * magnitudes_sum
