def count_nums(arr):
    count = 0
    for num in arr:
        digits_sum = sum(int(d) for d in str(num) if d.isdigit())
        if digits_sum > 0:
            count += 1
    return count
