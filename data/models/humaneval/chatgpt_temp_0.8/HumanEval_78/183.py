def hex_key(num):
    # Create a dictionary with keys as hexadecimal digits and values as their decimal equivalents
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    # Initialize a variable to keep track of the count of prime digits
    prime_count = 0
    
    # Loop through each character in the input string
    for char in num:
        # Convert the character to its decimal equivalent using the hex_dict dictionary
        decimal = hex_dict[char]
        
        # Check if the decimal equivalent is a prime digit
        if decimal in [2, 3, 5, 7, 11, 13, 17]:
            prime_count += 1
    
    # Return the count of prime digits
    return prime_count
