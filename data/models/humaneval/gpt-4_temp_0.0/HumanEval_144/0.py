def simplify(x, n):
    def fraction_to_float(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)

    result = x_float * n_float

    return result.is_integer()
