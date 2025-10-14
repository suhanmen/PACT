def specialFilter(nums):
    count = 0 # Initialize a counter variable to keep track of the number of elements that meet the criteria
    
    # Loop through each element in the input array
    for num in nums:
        # Convert the number to a string to access the first and last digits
        num_str = str(num)
        
        # Check if the number is greater than 10 and the first and last digits are odd
        if num > 10 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
            count += 1 # If the criteria are met, increment the counter variable
    
    return count # Return the final count of elements that meet the criteria
