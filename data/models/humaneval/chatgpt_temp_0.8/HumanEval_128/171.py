def prod_signs(arr):
    if not arr:
        return None
    
    product = 1
    magnitude_sum = 0
    
    for num in arr:
        if num == 0:
            product = 0
        else:
            product *= num / abs(num)
            magnitude_sum += abs(num)
    
    return int(product * magnitude_sum)
