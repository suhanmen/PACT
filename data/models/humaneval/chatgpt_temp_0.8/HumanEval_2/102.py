def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Get the integer part of the number
    integer_part = int(number)
    
    # Get the decimal part of the number
    decimal_part = number - integer_part
    
    # Return the decimal part of the number
    return decimal_part
