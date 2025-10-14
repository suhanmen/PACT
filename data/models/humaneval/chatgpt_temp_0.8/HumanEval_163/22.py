def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []
    
    # Check if a is greater than b, if so, swap their values
    if a > b:
        a, b = b, a
    
    # Loop through the range of a to b (inclusive)
    for i in range(a, b+1):
        # Check if the current number has even digits
        if all(int(digit) % 2 == 0 for digit in str(i)):
            even_digits.append(i)
    
    return even_digits
