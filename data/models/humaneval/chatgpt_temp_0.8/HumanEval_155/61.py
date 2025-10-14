def even_odd_count(num):
    even_count, odd_count = 0, 0
    num = abs(num)  # convert negative input to positive
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return (even_count, odd_count)
