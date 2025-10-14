def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            first_digit = str(num)[0]
            last_digit = str(num)[-1]
            if int(first_digit) % 2 != 0 and int(last_digit) % 2 != 0:
                count += 1
    return count
