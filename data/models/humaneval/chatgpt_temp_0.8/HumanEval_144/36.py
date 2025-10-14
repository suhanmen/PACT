def simplify(x, n):
    # Convert the fractions to integers
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # Multiply the numerators and denominators
    num = x_num * n_num
    denom = x_denom * n_denom

    # Check if the result is a whole number
    if num % denom == 0:
        return True
    else:
        return False
