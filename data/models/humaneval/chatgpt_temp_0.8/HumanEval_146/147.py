def specialFilter(nums):
    count = 0
    for num in nums:
        digits = str(abs(num))
        if len(digits) > 1 and int(digits[0]) % 2 != 0 and int(digits[-1]) % 2 != 0 and num > 10:
            count += 1
    return count
