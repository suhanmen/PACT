def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    num = float(value)
    floor_num = int(num)
    ceiling_num = floor_num + 1
    if abs(num - floor_num) < abs(num - ceiling_num):
        return floor_num
    elif abs(num - floor_num) > abs(num - ceiling_num):
        return ceiling_num
    else:
        if num > 0:
            return ceiling_num
        else:
            return floor_num
