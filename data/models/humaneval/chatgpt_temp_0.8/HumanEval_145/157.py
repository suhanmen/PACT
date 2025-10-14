def order_by_points(nums):
    def digit_sum(n):
        return sum(map(int, str(abs(n))))

    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
