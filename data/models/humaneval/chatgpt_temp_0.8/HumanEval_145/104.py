def order_by_points(nums):
    def sum_of_digits(num):
        """
        Returns the sum of digits of the given number.
        """
        return sum(int(digit) for digit in str(num) if digit.isdigit())

    # Sort the list based on the sum of digits and the index
    return sorted(nums, key=lambda num: (sum_of_digits(num), nums.index(num)))
