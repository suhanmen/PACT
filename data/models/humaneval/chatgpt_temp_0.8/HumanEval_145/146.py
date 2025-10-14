def order_by_points(nums):
    def sum_of_digits(num):
        return sum(map(int, str(abs(num))))

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
