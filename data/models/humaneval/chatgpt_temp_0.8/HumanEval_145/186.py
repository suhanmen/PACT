def order_by_points(nums):
    sums = []
    for i, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(abs(num)))
        sums.append((digit_sum, i, num))
    
    sorted_sums = sorted(sums)
    return [num for _, _, num in sorted_sums]
