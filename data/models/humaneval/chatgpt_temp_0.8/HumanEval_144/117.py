def simplify(x, n):
    num1, denom1 = x.split("/")
    num2, denom2 = n.split("/")
    numerator = int(num1) * int(num2)
    denominator = int(denom1) * int(denom2)
    result = numerator / denominator
    return result.is_integer()
