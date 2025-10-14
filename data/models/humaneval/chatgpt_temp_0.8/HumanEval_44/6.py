def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    # Ensure base is less than 10
    if base >= 10:
        return "Error: base should be less than 10"
      
    # Initialize variables
    result = ""
    quotient = x
    
    # Convert to new base
    while quotient > 0:
        remainder = quotient % base
        result = str(remainder) + result
        quotient = quotient // base
    
    return result
