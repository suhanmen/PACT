def specialFilter(nums):
    count = 0
    for num in nums:
        str_num = str(num)
        if len(str_num) > 1 and str_num[0] in ['1', '3', '5', '7', '9'] and str_num[-1] in ['1', '3', '5', '7', '9'] and num > 10:
            count += 1
    return count
