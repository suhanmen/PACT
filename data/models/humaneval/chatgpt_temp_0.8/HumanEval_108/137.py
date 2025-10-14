def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            digits = [int(digit) for digit in str(num)[1:]]
            digits[0] *= -1
            if sum(digits) > 0:
                count += 1
        else:
            if sum(int(digit) for digit in str(num)) > 0:
                count += 1
    return count
