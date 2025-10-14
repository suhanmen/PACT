def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            digits = [int(d) for d in str(num)[1:]]
            digits[0] = -digits[0]
        else:
            digits = [int(d) for d in str(num)]
        if sum(digits) > 0:
            count += 1
    return count
