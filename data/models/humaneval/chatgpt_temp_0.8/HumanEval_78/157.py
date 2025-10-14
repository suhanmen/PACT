def hex_key(num):
    prime_digits = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
        elif digit.isdigit():
            n = int(digit)
            if n > 1:
                prime = True
                for i in range(2, int(n**0.5)+1):
                    if n % i == 0:
                        prime = False
                        break
                if prime:
                    count += 1
    return count
