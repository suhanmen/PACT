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
    def get_digits(num):
        """
        Helper function to get signed digits of a number.
        """
        digits = []
        if num < 0:
            digits.append(-1)
            num *= -1
        while num > 0:
            digits.append(num % 10)
            num //= 10
        return digits[::-1] # Reverses the list of digits to maintain the original order.

    count = 0
    for num in arr:
        if sum(get_digits(num)) > 0: # Checks if the sum of signed digits is > 0.
            count += 1
    return count
