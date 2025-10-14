def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            # if number is negative, get the first signed digit and check if it's not 0
            signed_digit = int(str(num)[1])
            if signed_digit != 0:
                count += 1
        else:
            # if number is positive, check if the sum of its digits is greater than 0
            if sum(int(digit) for digit in str(num)) > 0:
                count += 1
    return count
