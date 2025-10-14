def specialFilter(nums):
    count = 0
    for num in nums:
        num_str = str(abs(num)) # convert the absolute value of number to string
        first_digit = int(num_str[0])
        last_digit = int(num_str[-1])
        if len(num_str) > 1 and num > 10 and first_digit % 2 == 1 and last_digit % 2 == 1:
            count += 1
    return count
