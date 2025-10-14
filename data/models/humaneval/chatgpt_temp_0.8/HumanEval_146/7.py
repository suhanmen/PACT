def specialFilter(nums):
    count = 0
    for num in nums:
        # Check if the number is greater than 10
        if num > 10:
            # Convert the number to a string to access its first and last digits
            num_str = str(num)
            # Check if both the first and last digits are odd
            if int(num_str[0]) % 2 == 1 and int(num_str[-1]) % 2 == 1:
                count += 1
    return count
