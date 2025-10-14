def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    # create an empty string to store the result
    result = ""
    
    # a loop to perform the conversion
    while x > 0:
        # get the remainder when x is divided by the new base
        remainder = x % base
        # add the remainder to the result
        result = str(remainder) + result
        # reduce x by dividing with the new base
        x //= base
    
    # return the result
    return result
