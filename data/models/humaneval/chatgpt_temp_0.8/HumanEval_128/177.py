def prod_signs(arr):
    if not arr:
        return None
    
    product = 1
    sum_of_magnitudes = 0
    
    for num in arr:
        if num == 0:
            continue
        product *= num/abs(num)
        sum_of_magnitudes += abs(num)
    
    return product * sum_of_magnitudes
