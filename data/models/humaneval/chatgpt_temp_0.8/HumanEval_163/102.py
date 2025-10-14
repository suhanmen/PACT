def generate_integers(a, b):
    # Ensure a is smaller than b
    if a > b:
        a, b = b, a
    # Initialize empty list to store even digits
    even_digits = []
    # Iterate through range of numbers including a and b
    for num in range(a, b+1):
        # Convert number to string to check each digit
        num_str = str(num)
        # Iterate through each digit in number
        for digit_str in num_str:
            # Check if digit is even and not already in even_digits list
            if int(digit_str) % 2 == 0 and int(digit_str) not in even_digits:
                # Append even digit to list
                even_digits.append(int(digit_str))
    # Sort even_digits list in ascending order
    even_digits.sort()
    return even_digits
