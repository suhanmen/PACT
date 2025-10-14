def count_nums(arr):
    count = 0
    for num in arr:
        if num >= 0:
            sum_of_digits = sum(int(digit) for digit in str(num))
        else:
            sum_of_digits = -1 * sum(int(digit) for digit in str(abs(num))) # get sum of digits for negative numbers
        if sum_of_digits > 0:
            count += 1
    return count
