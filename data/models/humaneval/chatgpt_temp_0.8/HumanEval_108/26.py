def count_nums(arr):
    def sum_of_digits(n):
        if n == 0:
            return 0
        elif n < 0:
            n = -n
            sign = -1
        else:
            sign = 1
        return sign * (n % 10) + sum_of_digits(n // 10)

    count = 0
    for num in arr:
        if sum_of_digits(num) != 0:
            count += 1
    return count
