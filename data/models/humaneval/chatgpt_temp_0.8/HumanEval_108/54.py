def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        signed_digits = [int(d) for d in str(num)]
        if num < 0:
            signed_digits = signed_digits[1:]
            signed_digits[0] = -signed_digits[0]
        if sum(signed_digits) > 0:
            count += 1
    return count
