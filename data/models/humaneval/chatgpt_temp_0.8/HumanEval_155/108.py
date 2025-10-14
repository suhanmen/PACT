def even_odd_count(num):
    even_digits = 0
    odd_digits = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
    if num < 0:
        even_digits *= -1
        odd_digits *= -1
    return (even_digits, odd_digits)
