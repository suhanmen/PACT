from fractions import Fraction   # import the Fraction class from the fractions module

def simplify(x, n):
    # convert the string representations of x and n to Fraction objects
    x_frac = Fraction(x)
    n_frac = Fraction(n)

    # multiply the two fractions
    product = x_frac * n_frac

    # check if the resulting fraction is reducible to a whole number
    return product == product.numerator
