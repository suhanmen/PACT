def hex_key(num):
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in prime_hex_digits:
            count += 1
        elif digit.isdigit():
            decimal_value = int(digit)
            if decimal_value > 1:
                is_prime = True
                for i in range(2, decimal_value):
                    if decimal_value % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    count += 1
    return count
