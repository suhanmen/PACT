def prod_signs(arr):
    if not arr:
        return None
    
    product = 1

    for n in arr:
        if n > 0:
            product *= 1
        elif n < 0:
            product *= -1

    return sum(abs(n) for n in arr) * product
