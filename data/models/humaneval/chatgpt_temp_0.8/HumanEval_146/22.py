def specialFilter(nums):
    count = 0
    
    for num in nums:
        # Check if number is greater than 10
        if num > 10:
            # Convert number to positive integer
            num = abs(num)
            # Check if first and last digits are odd
            first_digit = int(str(num)[0])
            last_digit = int(str(num)[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
                
    return count
