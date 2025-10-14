def count_nums(arr):
    def sum_of_digits(num):
        """
        Calculates the sum of the digits of a given number
        """
        if num == 0:
            return 0
        elif num < 0:
            num = -num
            sign = -1
        else:
            sign = 1
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return sign * total

    count = 0
    for num in arr:
        if sum_of_digits(num) != 0:
            count += 1
    return count
