def count_nums(arr):
    count = 0
    for num in arr:
        sum_of_digits = 0
        for digit in str(num):
            if digit.isdigit():
                sum_of_digits += int(digit)
            elif digit == '-':
                sum_of_digits -= 1
        if sum_of_digits > 0:
            count += 1
    return count
