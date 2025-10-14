def specialFilter(nums):
    count = 0 # initialize a variable to keep track of count
    for num in nums: # iterate through the array
        if num > 10 and str(num)[0] in ['1', '3', '5', '7', '9'] and str(num)[-1] in ['1', '3', '5', '7', '9']:
            # check if the number is greater than 10 and first and last digits are odd
            count += 1 # increment the count
    return count # return the final count
