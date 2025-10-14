def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    """
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))
    
    return sorted(nums, key=lambda num: (digit_sum(num), nums.index(num)))
