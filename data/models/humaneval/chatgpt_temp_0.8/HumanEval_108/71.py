def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        signed_digits_sum = sum(int(digit) for digit in str(num) if digit.isdigit() or digit == '-')
        if signed_digits_sum > 0:
            count += 1
    return count
