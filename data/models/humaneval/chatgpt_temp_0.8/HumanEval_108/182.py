def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        if num < 0:
            num = str(num)[1:]
            if int(num[0]) > 0:
                count += 1
        else:
            num = str(num)
        digit_sum = sum(int(d) for d in num)
        if digit_sum > 0:
            count += 1
    return count
