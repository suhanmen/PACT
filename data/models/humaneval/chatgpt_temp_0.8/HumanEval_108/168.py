def count_nums(arr):
    def sum_digits(num):
        if num == 0:
            return 0
        elif num < 0:
            num = -num
            sign = -1
        else:
            sign = 1
        return sign * (num % 10) + sum_digits(num // 10)

    return sum(1 for num in arr if sum_digits(num) != 0)
