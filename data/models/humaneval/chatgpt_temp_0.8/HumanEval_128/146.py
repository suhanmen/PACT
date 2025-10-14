def prod_signs(arr):
    if not arr:
        return None
    
    prod = 1
    sum_magnitudes = 0
    
    for num in arr:
        if num == 0:
            continue
        prod *= 1 if num > 0 else -1
        sum_magnitudes += abs(num)
    
    return prod * sum_magnitudes
