def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    # Split the string representations of x and n into numerator and denominator
    x_num, x_denom = x.split('/')
    n_num, n_denom = n.split('/')
    
    # Calculate the numerator and denominator of the simplified fraction
    new_num = int(x_num) * int(n_num)
    new_denom = int(x_denom) * int(n_denom)
    
    # Check if the simplified fraction is a whole number
    if new_num % new_denom == 0:
        return True
    else:
        return False
