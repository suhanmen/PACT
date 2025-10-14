def count_nums(arr):
    count = 0
    for num in arr:
        digit_sum = sum(map(int, str(num).replace('-', '')))
        if digit_sum > 0:
            count += 1
    return count
