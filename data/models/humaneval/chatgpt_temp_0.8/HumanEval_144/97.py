def simplify(x, n):
    # Converting the string representations of fractions to actual fractions
    x = Fraction(x)
    n = Fraction(n)
    
    # Calculating the product of the fractions
    product = x * n
    
    # Checking if the product evaluates to a whole number
    if product == int(product):
        return True
    else:
        return False
