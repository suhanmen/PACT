def simplify(x, n):
    # convert the fractions to integers
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # multiply the numerators and denominators
    result_num = x_num * n_num
    result_denom = x_denom * n_denom

    # check if the result is a whole number
    if result_num % result_denom == 0:
        return True
    else:
        return False
