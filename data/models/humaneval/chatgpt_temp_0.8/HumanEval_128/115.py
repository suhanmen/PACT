def prod_signs(arr):
    if not arr:  # if arr is empty
        return None
    
    prod = 1
    magnitude_sum = 0

    for num in arr:
        if num == 0:
            continue
        prod *= num / abs(num)  # get the sign of the number
        magnitude_sum += abs(num)

    return int(prod * magnitude_sum)
