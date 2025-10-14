def even_odd_count(num):
    even_count = 0
    odd_count = 0
    num = abs(num)  # get absolute value to handle negative numbers
    while num > 0:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10  # remove the last digit
    return (even_count, odd_count)
