def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:    # if input number is 0, return 0 in the new base
        return '0'
    result = ''   # initialize result variable
    while x > 0:
        remainder = x % base    # calculate remainder after division
        result = str(remainder) + result   # add remainder to result
        x //= base   # divide x by base and set the result as new x
    return result
