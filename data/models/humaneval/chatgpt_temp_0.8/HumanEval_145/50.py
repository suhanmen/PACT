def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    # Create a list of tuples, where each tuple contains the number, its digit sum, and its index.
    nums_with_sums = [(num, digit_sum(num), i) for i, num in enumerate(nums)]

    # Sort the list by digit sum first, then by index.
    sorted_nums = sorted(nums_with_sums, key=lambda x: (x[1], x[2]))

    # Return a list of the sorted numbers.
    return [num for num, _, _ in sorted_nums]
