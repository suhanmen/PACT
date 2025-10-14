def count_nums(arr):
    count = 0
    for num in arr:
        digit_sum = sum(int(d) for d in str(abs(num)))
        if num < 0:
            digit_sum *= -1
        if digit_sum > 0:
            count += 1
    return count
