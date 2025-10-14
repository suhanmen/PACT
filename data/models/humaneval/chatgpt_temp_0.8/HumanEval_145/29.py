def order_by_points(nums):
    def get_sum_of_digits(num):
        return sum([int(d) for d in str(abs(num))])
    
    return sorted(nums, key=lambda x: (get_sum_of_digits(x), nums.index(x)))
