def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into an integer part
    (largest integer smaller than given number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    
    # Split the number into its integer and decimal parts
    integer_part = int(number)
    decimal_part = number - integer_part
    
    # Return only the decimal part
    return decimal_part
