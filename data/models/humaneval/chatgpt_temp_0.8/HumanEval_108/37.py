def count_nums(arr):
    count = 0
    for num in arr:
        if num >= 0:
            digit_sum = sum(int(digit) for digit in str(num))
        else:
            digit_sum = -sum(int(digit) for digit in str(num)[1:])
        if digit_sum > 0:
            count += 1
    return count
