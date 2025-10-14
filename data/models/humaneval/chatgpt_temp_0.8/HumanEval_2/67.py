def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Decompose the number into integer and decimal parts using the math library
    import math
    integer_part = math.floor(number)
    decimal_part = number - integer_part
    
    # Return the decimal part of the number
    return decimal_part
