def even_odd_count(num):
    even = 0
    odd = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    if num < 0:
        even = -even
        odd = -odd
    return (even, odd)
