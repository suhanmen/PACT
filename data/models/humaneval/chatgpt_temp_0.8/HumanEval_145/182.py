def order_by_points(nums):
    # Define a function to calculate the sum of digits
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    # Sort the list by digit sum and index
    return sorted(nums, key=lambda num: (digit_sum(num), nums.index(num)))
