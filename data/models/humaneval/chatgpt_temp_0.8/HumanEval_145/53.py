def order_by_points(nums):
    def digit_sum(num):
        return sum(int(d) for d in str(abs(num)))
    
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
