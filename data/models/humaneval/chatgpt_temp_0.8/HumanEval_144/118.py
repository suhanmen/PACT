def simplify(x, n):
    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))

    product = numerator_x * numerator_n
    divisor = denominator_x * denominator_n

    if product % divisor == 0:
        return True
    else:
        return False
