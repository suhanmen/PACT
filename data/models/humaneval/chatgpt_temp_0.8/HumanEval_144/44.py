from fractions import Fraction

def simplify(x, n):
    x_f = Fraction(x)
    n_f = Fraction(n)
    res = x_f * n_f
    return res == res // 1
