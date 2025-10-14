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

    # Ensure a is less than or equal to b
    if a > b:
        a, b = b, a

    # Loop through the numbers between a and b
    for num in range(a, b+1):
        # Convert the number to a string to access its digits
        num_str = str(num)
        # Loop through the digits and append the even ones
        for digit in num_str:
            if int(digit) % 2 == 0:
                result.append(int(digit))

    # Remove duplicates and sort the list
    result = sorted(list(set(result)))

    return result
