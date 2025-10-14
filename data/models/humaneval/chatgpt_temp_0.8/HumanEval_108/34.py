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
    def sum_of_digits(num):
        """
        Helper function which returns the sum of the digits of a number.
        For negative numbers, the first signed digit will be negative.
        """
        total = 0
        num_str = str(num)
        for i in range(1, len(num_str)):
            total += int(num_str[i])
        if num_str[0] == "-":
            total -= int(num_str[1])
        else:
            total += int(num_str[0])
        return total

    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count
