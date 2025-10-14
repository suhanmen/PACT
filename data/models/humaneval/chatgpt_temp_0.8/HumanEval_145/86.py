def order_by_points(nums):
    # Define a helper function to calculate the sum of digits in a number
    def sum_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    # Create a list of tuples with the original index and sum of digits for each number
    nums_with_sums = [(i, sum_digits(num), num) for i, num in enumerate(nums)]

    # Sort the list by sum of digits, then by original index
    nums_with_sums.sort(key=lambda x: (x[1], x[0]))

    # Extract just the original numbers in their new order
    return [num for _, _, num in nums_with_sums]
