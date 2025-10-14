def even_odd_count(num):
    evens = 0
    odds = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    if num < 0:
        evens *= -1
        odds *= -1
    return (evens, odds)
