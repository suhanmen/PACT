def order_by_points(nums):
    if not nums:
        return []

    def sum_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))
