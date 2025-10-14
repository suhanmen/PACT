def simplify(x, n):
    # Convert string fractions to tuples of integers
    x_num, x_denom = [int(num) for num in x.split('/')]
    n_num, n_denom = [int(num) for num in n.split('/')]

    # Multiply fractions
    result_num = x_num * n_num
    result_denom = x_denom * n_denom

    # Check if result is a whole number
    if result_num % result_denom == 0:
        return True
    else:
        return False
