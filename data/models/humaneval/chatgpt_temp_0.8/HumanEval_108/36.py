def count_nums(arr):
    def sum_digits(num):
        """
        Helper function to calculate the sum of digits in a number.
        """
        return sum(int(digit) for digit in str(num))

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
        elif num < 0 and sum_digits(num) < 0:
            count += 1
    return count
