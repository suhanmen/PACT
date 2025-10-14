def count_nums(arr):
    def sum_digits(n):
        """
        Helper function to compute the sum of digits of an integer.
        """
        return sum([int(d) for d in str(abs(n))])

    count = 0
    for n in arr:
        if sum_digits(n) > 0:
            count += 1
    return count
