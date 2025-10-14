def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        elif num < 0:
            digits = [int(d) for d in str(num)[1:]]
            digits.insert(0, -1)
        else:
            digits = [int(d) for d in str(num)]
        if sum(digits) > 0:
            count += 1
    return count
