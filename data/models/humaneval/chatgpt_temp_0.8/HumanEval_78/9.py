def hex_key(num):
    prime_hex = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in prime_hex:
            count += 1
        elif digit.isdigit():
            # Convert to decimal and check if it's prime
            decimal = int(digit, 16)
            if decimal > 1:
                for i in range(2, decimal):
                    if decimal % i == 0:
                        break
                else:
                    count += 1
    return count
