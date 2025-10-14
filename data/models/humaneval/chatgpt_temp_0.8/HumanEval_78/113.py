def hex_key(num):
    # create a list of hexadecimal digits that are primes
    primes = ['2', '3', '5', '7', 'B', 'D']
    # initialize a counter variable
    count = 0
    # iterate over each character in the input string
    for char in num:
        # if the character is in the list of primes, increment the count
        if char in primes:
            count += 1
    # return the count
    return count
