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
    def signed_digits(num):
        """
        Helper function to calculate signed digits of a number.
        """
        num_str = str(num)
        digits = []
        for i, c in enumerate(num_str):
            if c.isdigit():
                digits.append(int(c))
            elif i == 0:
                digits.append(-int(c))
        return digits

    count = 0
    for num in arr:
        digit_sum = sum(signed_digits(num))
        if digit_sum > 0:
            count += 1
    return count
