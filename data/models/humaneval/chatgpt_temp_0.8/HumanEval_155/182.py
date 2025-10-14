def even_odd_count(num):
    even = 0
    odd = 0
    num_str = str(abs(num))
    for digit in num_str:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    if num < 0:
        even, odd = odd, even
    return (even, odd)
