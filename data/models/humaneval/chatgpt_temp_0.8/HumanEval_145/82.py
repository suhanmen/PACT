def order_by_points(nums):
    nums_with_sum_of_digits = [(num, sum(int(digit) for digit in str(abs(num)))) for num in nums]
    sorted_nums = sorted(nums_with_sum_of_digits, key=lambda x: (x[1], nums.index(x[0])))
    return [num[0] for num in sorted_nums]
