def prod_signs(arr):
    if not arr:
        return None
    
    prod = 1
    sum_magnitudes = 0
    
    for num in arr:
        if num == 0:
            prod = 0
        else:
            prod *= num / abs(num)
            sum_magnitudes += abs(num)
    
    return int(prod * sum_magnitudes)
