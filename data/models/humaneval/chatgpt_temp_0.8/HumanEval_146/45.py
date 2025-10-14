def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(num)
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count
