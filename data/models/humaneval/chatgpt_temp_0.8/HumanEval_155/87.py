def even_odd_count(num):
    even_digits = 0
    odd_digits = 0
    num = abs(num)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        num = num // 10
    return (even_digits, odd_digits)
