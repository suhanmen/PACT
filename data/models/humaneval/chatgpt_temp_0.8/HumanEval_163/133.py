def generate_integers(a, b):
    # swap a and b if a is greater than b
    if a > b:
        a, b = b, a
    
    # initialize an empty list to store the even digits
    result = []
    
    # iterate over the range of integers between a and b
    for num in range(a, b+1):
        # convert the integer to a string for digit-wise processing
        digits = str(num)
        # iterate over the digits of the integer
        for digit in digits:
            # check if the digit is even and not already in the result list
            if int(digit) % 2 == 0 and int(digit) not in result:
                # add the even digit to the result list
                result.append(int(digit))
    
    # sort the result list in ascending order and return it
    result.sort()
    return result
