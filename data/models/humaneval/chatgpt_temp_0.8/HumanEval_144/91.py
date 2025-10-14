def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    result = num1 * num2 / (den1 * den2)
    return result.is_integer()
