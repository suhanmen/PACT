def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    return sorted(nums, key=lambda n: (digit_sum(n), nums.index(n)))

