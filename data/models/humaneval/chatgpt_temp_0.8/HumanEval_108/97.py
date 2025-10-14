def count_nums(arr):
    def sum_digits(n):
        """
        Compute the sum of the digits of a number.
        """
        if n == 0:
            return 0
        elif n < 0:
            return -sum_digits(-n)
        else:
            return n % 10 + sum_digits(n // 10)

    return len([x for x in arr if sum_digits(x) > 0])
