def generate_integers(a, b):
    # Swap a and b if a is greater than b
    if a > b:
        a, b = b, a
    
    # Initialize an empty list to store the even digits
    even_digits = []
    
    # Loop through the range from a to b (inclusive)
    for num in range(a, b+1):
        # Check if the current number has any even digits
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))
                break # Break out of the inner loop if an even digit is found
        
    # Sort the even digits in ascending order and return them
    return sorted(even_digits)
