def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def signed_digits(n):
        """
        Helper function to calculate the signed digits of a number.
        """
        if n == 0:
            return [0]
        digits = []
        while n != 0:
            digits.append(n % 10)
            n //= 10
        if digits[-1] < 0:
            digits[-1] = -digits[-1]
            digits[-2] = -(digits[-2] - 1)
        return digits[::-1]

    count = 0
    for num in arr:
        if sum(signed_digits(num)) > 0:
            count += 1
    return count
