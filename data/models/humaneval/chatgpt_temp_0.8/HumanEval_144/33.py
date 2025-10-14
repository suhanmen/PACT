def simplify(x, n):
    numerator_x, denominator_x = map(int, x.split("/"))
    numerator_n, denominator_n = map(int, n.split("/"))
    result = numerator_x * numerator_n / (denominator_x * denominator_n)
    return result.is_integer()
