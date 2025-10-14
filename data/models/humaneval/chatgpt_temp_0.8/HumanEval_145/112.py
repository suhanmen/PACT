def order_by_points(nums):
    def sum_of_digits(num):
        return sum(int(d) for d in str(abs(num)))

    return sorted(nums, key=lambda num: (sum_of_digits(num), nums.index(num)))

