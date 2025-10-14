def multiply(a, b):
    # Get the unit digits of a and b
    unit_a = abs(a) % 10
    unit_b = abs(b) % 10
    
    # Multiply the unit digits
    product = unit_a * unit_b
    
    return product
