def order_by_points(nums):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    nums_with_sum = [(num, sum_of_digits(num), i) for i, num in enumerate(nums)]
    nums_with_sum.sort(key=lambda x: (x[1], x[2]))
    return [num for num, _, _ in nums_with_sum]
