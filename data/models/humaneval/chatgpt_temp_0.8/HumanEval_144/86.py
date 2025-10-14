def simplify(x, n):
    numerator_1, denominator_1 = map(int, x.split('/'))
    numerator_2, denominator_2 = map(int, n.split('/'))
    product = numerator_1 * numerator_2
    divisor = denominator_1 * denominator_2
    if product % divisor == 0:
        return True
    else:
        return False
