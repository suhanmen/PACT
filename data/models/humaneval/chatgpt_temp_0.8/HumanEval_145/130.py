def order_by_points(nums):
    # Create a dictionary to hold the sum of digits for each number
    nums_dict = {}
    for i, num in enumerate(nums):
        nums_dict[i] = sum(int(digit) for digit in str(abs(num)))

    # Sort the dictionary based on the sum of digits and then by index
    sorted_dict = sorted(nums_dict.items(), key=lambda x: (x[1], x[0]))

    # Create a new list with the sorted numbers
    sorted_nums = [nums[i] for i, _ in sorted_dict]

    return sorted_nums
