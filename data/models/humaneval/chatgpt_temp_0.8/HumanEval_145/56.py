def order_by_points(nums):
    def sum_digits(n):
        return sum(int(d) for d in str(abs(n)))
    
    return sorted(nums, key=lambda n: (sum_digits(n), nums.index(n)))
