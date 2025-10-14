def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Ensure a is the smaller number
    if a > b:
        a, b = b, a

    # Initialize the result list
    result = []

    # Iterate through the range of numbers between a and b
    for i in range(a, b + 1):
        # Check if the number is even
        if i % 2 == 0:
            # Add the even number to the result list
            result.append(i)

    return result