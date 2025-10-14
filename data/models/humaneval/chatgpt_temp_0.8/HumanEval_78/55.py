def hex_key(num):
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_hex_digits:
            decimal_value = int(digit, 16)
            if decimal_value <= 1:
                continue
            for i in range(2, int(decimal_value ** 0.5) + 1):
                if decimal_value % i == 0:
                    break
            else:
                count += 1
    return count
