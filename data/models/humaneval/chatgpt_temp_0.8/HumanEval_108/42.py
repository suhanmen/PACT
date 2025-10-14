def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        if num < 0:
            digits = [int(d) for d in str(num)[1:] if d.isdigit()]
            digits.insert(0, -1 * int(str(num)[0]))
        else:
            digits = [int(d) for d in str(num) if d.isdigit()]
        if sum(digits) > 0:
            count += 1
    return count
