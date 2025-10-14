def order_by_points(nums):
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    nums_with_scores = [(num, digit_sum(num), index) for index, num in enumerate(nums)]
    nums_with_scores.sort(key=lambda x: (x[1], x[2]))
    return [num for num, _, _ in nums_with_scores]
