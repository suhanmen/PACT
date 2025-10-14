def specialFilter(nums):
    count = 0
    for num in nums:
        str_num = str(abs(num)) # convert to positive and then to string
        if len(str_num) > 1 and int(str_num[0])%2 == 1 and int(str_num[-1])%2 == 1 and num > 10:
            count += 1
    return count
