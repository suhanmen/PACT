def hex_key(num):
    primes = ["2", "3", "5", "7", "B", "D"]
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit():
            if int(digit) > 1:
                for i in range(2, int(digit)):
                    if int(digit) % i == 0:
                        break
                else:
                    count += 1
    return count
