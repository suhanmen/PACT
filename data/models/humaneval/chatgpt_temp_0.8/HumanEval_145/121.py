def order_by_points(nums):
    def digit_sum(num):
        return sum(int(d) for d in str(abs(num)))  # sum of the digits of a number

    return sorted(nums, key=lambda num: (digit_sum(num), nums.index(num)))
