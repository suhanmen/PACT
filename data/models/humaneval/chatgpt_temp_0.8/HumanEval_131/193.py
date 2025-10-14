def digits(n):
    odd_digit_product = 1
    even_digit_count = 0
    
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            odd_digit_product *= digit
        else:
            even_digit_count += 1
        n //= 10
        
    if even_digit_count == len(str(n)):
        return 0
    else:
        return odd_digit_product
