def order_by_points(nums):
    # define a function to calculate the sum of digits of a number
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))
    
    # sort the list based on the sum of digits and the original index
    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
