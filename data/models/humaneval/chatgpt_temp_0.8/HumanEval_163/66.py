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

    # Swap a and b if a > b
    if a > b:
        a, b = b, a

    # Loop through every number between a and b
    for num in range(a, b+1):
        # Convert the number to a string so we can access its digits
        num_str = str(num)
        # Loop through every digit in the number
        for digit in num_str:
            # Check if the digit is even and not already in the result list
            if int(digit) % 2 == 0 and int(digit) not in result:
                result.append(int(digit))

    return result
