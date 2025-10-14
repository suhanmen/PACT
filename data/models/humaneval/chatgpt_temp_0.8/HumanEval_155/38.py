def even_odd_count(num):
    even_count = 0
    odd_count = 0
    
    # Convert number to positive if it is negative
    if num < 0:
        num = -num
    
    # Count the number of even and odd digits
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    
    return (even_count, odd_count)
