def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        signed_digits_sum = 0
        for digit in str(abs(num)):
            signed_digits_sum += int(digit)
        if num < 0:
            signed_digits_sum *= -1
        if signed_digits_sum != 0:
            count += 1
    return count
