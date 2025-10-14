def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    if denom1 % num1 == 0 and denom2 % num2 == 0:
        return num1 * (denom2 // num2) == denom1 * (denom2 // num2)
    elif denom1 % num1 == 0:
        return denom2 % (num2 * (denom1 // num1)) == 0
    elif denom2 % num2 == 0:
        return denom1 % (num1 * (denom2 // num2)) == 0
    else:
        return False
