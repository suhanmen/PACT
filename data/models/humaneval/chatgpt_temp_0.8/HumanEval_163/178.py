def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    if a > b:
        a, b = b, a  # swap a and b if a > b
    for i in range(a, b+1):
        digits = [int(d) for d in str(i) if int(d) % 2 == 0]  # get even digits of i
        result.extend(digits)  # add even digits to result list
    return result
