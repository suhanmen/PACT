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
        a, b = b, a # Swap a and b if a is greater than b
        
    for num in range(a, b+1):
        for char in str(num):
            if int(char) % 2 == 0 and int(char) not in result:
                result.append(int(char))
    return result
