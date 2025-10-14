def hex_key(num):
    primes = [2, 3, 5, 7, 11, 13, 17] #list of prime numbers
    count = 0 #initialize count to 0
    for digit in num:
        if digit in ['2', '3', '5', '7', 'B', 'D']:
            #if the digit is prime, increment the count
            count += 1
    return count
