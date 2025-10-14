def order_by_points(nums):
    def sum_digits(n):
        return sum(int(digit) for digit in str(n))

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))
