def count_nums(arr):
    cnt = 0
    for num in arr:
        digits_sum = sum(int(d) for d in str(num) if d.isdigit())
        if digits_sum > 0:
            cnt += 1
    return cnt
