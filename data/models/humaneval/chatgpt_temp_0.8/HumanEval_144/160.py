def simplify(x, n):
    # Convert x and n to numerator and denominator integers
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    # Multiply numerator and denominator of x * n
    res_num = x_num * n_num
    res_den = x_den * n_den
    # Check if the result is a whole number
    return res_num % res_den == 0
