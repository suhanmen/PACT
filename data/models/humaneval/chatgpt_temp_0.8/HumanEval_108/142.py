def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        if num < 0:
            num = str(num)[1:]
            if int(num[0]) != 0:
                count += 1
        else:
            num = str(num)
        if sum([int(digit) for digit in num]) > 0:
            count += 1
    return count
