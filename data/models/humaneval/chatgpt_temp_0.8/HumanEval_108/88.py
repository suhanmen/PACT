def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        digits_sum = sum(int(digit) for digit in str(abs(num)))
        if digits_sum > 0:
            count += 1
    return count
