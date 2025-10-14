def multiply(a, b):
    # Get the unit digit of each number
    a_digit = abs(a) % 10
    b_digit = abs(b) % 10
    
    # Multiply the digits together
    product = a_digit * b_digit
    
    # Handle the case where one or both inputs are negative
    if a < 0 and b < 0:
        return product
    elif a < 0 or b < 0:
        return -product
    else:
        return product
