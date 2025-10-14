def count_nums(arr):
    count = 0
    for num in arr:
        digits_sum = sum(map(int, str(num)))
        if digits_sum != 0:
            count += 1
        elif digits_sum == 0 and str(num)[0] == "-":
            count += 1
    return count
