def order_by_points(nums):
    def digit_sum(num):
        return sum(map(int, str(abs(num))))

    nums_with_sums = [(num, digit_sum(num), i) for i, num in enumerate(nums)]
    sorted_nums = sorted(nums_with_sums, key=lambda x: (x[1], x[2]))
    return [num for num, _, _ in sorted_nums]
