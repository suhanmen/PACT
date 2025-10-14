def specialFilter(nums):
    count = 0
    for num in nums:
        # check if the number is greater than 10
        if num > 10:
            # convert the number to a string to access the first and last digits
            str_num = str(num)
            # check if both first and last digits are odd
            if int(str_num[0]) % 2 != 0 and int(str_num[-1]) % 2 != 0:
                count += 1
    return count
