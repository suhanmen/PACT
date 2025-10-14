def specialFilter(nums):
    count = 0 # initialize counter
    for num in nums:
        if num > 10:
            first = int(str(num)[0]) # get first digit
            last = int(str(num)[-1]) # get last digit
            if first % 2 != 0 and last % 2 != 0: # check if both digits are odd
                count += 1 # increment counter
    return count
