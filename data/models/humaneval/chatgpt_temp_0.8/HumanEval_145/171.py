def order_by_points(nums):
    def digit_sum(num):
        # calculate the sum of digits of a given number
        return sum(int(d) for d in str(abs(num)))

    # create a list of tuples with the original index and digit sum
    nums_with_sum = [(i, digit_sum(n)) for i, n in enumerate(nums)]
    
    # sort the list of tuples by digit sum and then by original index
    sorted_nums = sorted(nums_with_sum, key=lambda x: (x[1], x[0]))
    
    # return the sorted list of integers
    return [nums[i] for i, _ in sorted_nums]
