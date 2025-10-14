def count_nums(arr):
    def sum_digits(n):
        return sum(map(int, str(abs(n))))

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count
