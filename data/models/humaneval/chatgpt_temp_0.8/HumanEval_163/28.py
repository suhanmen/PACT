def generate_integers(a, b):
    even_digits = []
    
    # Swap a and b if a is larger than b
    if a > b:
        a, b = b, a
    
    for num in range(a, b+1):
        # Convert number to string for easy indexing
        num_str = str(num)
        for digit in num_str:
            # Check if digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))
    
    return even_digits
