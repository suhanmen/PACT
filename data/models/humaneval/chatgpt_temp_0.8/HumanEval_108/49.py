def count_nums(arr):
    def sum_digits(n):
        s = 0
        for d in str(abs(n)):
            s += int(d)
        return s if n > 0 else -s

    count = 0
    for num in arr:
        if sum_digits(num) != 0:
            count += 1
    return count
