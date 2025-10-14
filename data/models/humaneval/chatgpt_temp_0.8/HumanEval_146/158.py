def specialFilter(nums):
    count = 0
    for num in nums:
        str_num = str(num)
        if len(str_num) > 1 and int(str_num[0]) % 2 != 0 and int(str_num[-1]) % 2 != 0 and num > 10:
            count += 1
    return count
