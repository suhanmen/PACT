def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if int(num_str[0]) % 2 == 1 and int(num_str[-1]) % 2 == 1:
                count += 1
    return count
