def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        digits = [int(digit) for digit in str(abs(num))]
        if sum(digits) > 0:
            count += 1
    return count
