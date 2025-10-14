def count_nums(arr):
    def sum_of_digits(num):
        if num == 0:
            return 0
        elif num < 0:
            num = -num
            sign = -1
        else:
            sign = 1
        return sign * sum(int(digit) for digit in str(num))

    return sum(1 for num in arr if sum_of_digits(num) > 0)
