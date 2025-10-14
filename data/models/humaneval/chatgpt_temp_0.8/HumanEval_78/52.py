def hex_key(num):
    primes = {"2", "3", "5", "7", "B", "D"}
    count = 0
    for digit in num:
        if digit in primes:
            if int(digit, 16) <= 13:
                count += 1
            elif int(digit, 16) % 2 != 0 and int(digit, 16) % 3 != 0:
                i = 5
                while i**2 <= int(digit, 16):
                    if int(digit, 16) % i == 0 or int(digit, 16) % (i+2) == 0:
                        break
                    i += 6
                else:
                    count += 1
    return count
