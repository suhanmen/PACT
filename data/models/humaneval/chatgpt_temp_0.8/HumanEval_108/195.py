def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        digits = [int(d) for d in str(num) if d.isnumeric()]
        if sum(digits) > 0:
            count += 1
        elif sum(digits) == 0 and "-" in str(num):
            count += 1
    return count
