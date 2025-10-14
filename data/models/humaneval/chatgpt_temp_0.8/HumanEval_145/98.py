def order_by_points(nums):
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))
    
    return sorted(nums, key=lambda n: (sum_of_digits(n), nums.index(n)))
