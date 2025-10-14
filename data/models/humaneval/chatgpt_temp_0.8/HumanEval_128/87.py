def prod_signs(arr):
    if not arr:
        return None
    sign = 1
    result = 0
    for num in arr:
        if num == 0:
            sign = 0
        elif num < 0:
            sign *= -1  
        result += abs(num)
    return sign * result
