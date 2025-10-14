def count_nums(arr):
    def sum_digits(n):
        if n == 0:
            return 0
        elif n < 0:
            n = -n
            sign = -1
        else:
            sign = 1
        return sign * sum(int(digit) for digit in str(n))

    count = 0
    for num in arr:
        if sum_digits(num) != 0:
            count += 1
    return count
