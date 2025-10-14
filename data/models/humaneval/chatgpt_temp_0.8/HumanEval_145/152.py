def order_by_points(nums):
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
