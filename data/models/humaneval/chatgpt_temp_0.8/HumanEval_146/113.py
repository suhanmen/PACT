def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            digits = [int(digit) for digit in str(num)]
            if digits[0] % 2 == 1 and digits[-1] % 2 == 1:
                count += 1
    return count
