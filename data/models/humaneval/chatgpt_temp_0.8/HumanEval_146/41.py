def specialFilter(nums):
    count = 0
    for num in nums:
        # Check if first and last digits are odd
        first_digit = abs(num) // 10**(len(str(abs(num))) - 1)
        last_digit = abs(num) % 10
        if first_digit % 2 != 0 and last_digit % 2 != 0:
            # Check if number is greater than 10
            if abs(num) > 10:
                count += 1
    return count
