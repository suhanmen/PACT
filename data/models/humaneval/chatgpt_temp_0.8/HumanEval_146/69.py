def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(num)
            if num_str[0] in ['1', '3', '5', '7', '9'] and num_str[-1] in ['1', '3', '5', '7', '9']:
                count += 1
    return count
