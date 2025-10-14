def specialFilter(nums):
    count = 0
    for num in nums:
        str_num = str(abs(num)) # convert to string and take absolute value
        if len(str_num) == 1: # ignore single digit numbers
            continue
        if int(str_num[0]) % 2 != 0 and int(str_num[-1]) % 2 != 0 and num > 10: # check first and last digits
            count += 1
    return count
