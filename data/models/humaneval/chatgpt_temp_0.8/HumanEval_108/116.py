def count_nums(arr):
    count = 0
    for num in arr:
        signed_digits_sum = 0
        for digit in str(num):
            if digit == '-':
                signed_digits_sum -= int(digit + next(iter(str(num)[str(num).index('-')+1:])))
            else:
                signed_digits_sum += int(digit)
        if signed_digits_sum > 0:
            count += 1
    return count
