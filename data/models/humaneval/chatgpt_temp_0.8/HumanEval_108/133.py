def count_nums(arr):
    count = 0
    for num in arr:
        sum_digits = sum(int(d) for d in str(abs(num)))
        if sum_digits > 0:
            count += 1
    return count
