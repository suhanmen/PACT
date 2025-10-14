def order_by_points(nums):
    def get_sum_of_digits(num):
        if num < 0:
            num = -num
        sum_of_digits = 0
        while num > 0:
            sum_of_digits += num % 10
            num //= 10
        return sum_of_digits
    
    nums_with_scores = [(num, get_sum_of_digits(num), i) for i, num in enumerate(nums)]
    nums_with_scores.sort(key=lambda x: (x[1], x[2]))
    return [num for num, _, _ in nums_with_scores]
