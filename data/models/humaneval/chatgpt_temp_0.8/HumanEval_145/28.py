def order_by_points(nums):
    def sum_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=lambda num: (sum_digits(num), nums.index(num)))
