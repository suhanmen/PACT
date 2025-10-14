def count_nums(arr):
    count = 0
    for num in arr:
        digit_sum = sum(int(digit) for digit in str(abs(num)))
        signed_digit_sum = digit_sum
        if num < 0:
            signed_digit_sum *= -1
        if signed_digit_sum > 0:
            count += 1
    return count
