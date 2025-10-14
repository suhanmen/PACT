def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        elif num < 0:
            num = str(num)[1:]
            if num[0].isdigit():
                num = '-' + num
        sum_of_digits = sum(int(digit) for digit in str(num))
        if sum_of_digits > 0:
            count += 1
    return count
