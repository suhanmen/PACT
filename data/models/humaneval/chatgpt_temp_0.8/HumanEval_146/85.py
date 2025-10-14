def specialFilter(nums):
    count = 0
    for num in nums:
        string_num = str(num)
        first_digit = int(string_num[0])
        last_digit = int(string_num[-1])
        if num > 10 and first_digit % 2 != 0 and last_digit % 2 != 0:
            count += 1
    return count
