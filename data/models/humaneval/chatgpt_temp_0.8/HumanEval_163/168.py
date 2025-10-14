def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # create an empty list to store the even digits
    even_digits = []
    
    # loop through each number between a and b (inclusive)
    for num in range(a, b+1):
        
        # convert the number to a string so we can iterate over its digits
        num_str = str(num)
        
        # loop through each digit of the number
        for digit in num_str:
            
            # check if the digit is even
            if int(digit) % 2 == 0:
                
                # add the even digit to our list if it's not already there
                if int(digit) not in even_digits:
                    even_digits.append(int(digit))
    
    # sort the list of even digits in ascending order and return it
    return sorted(even_digits)
