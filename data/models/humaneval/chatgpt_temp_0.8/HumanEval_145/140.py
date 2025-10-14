def order_by_points(nums):
    sorted_nums = sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x))), nums.index(x)))
    return sorted_nums
