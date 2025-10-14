def simplify(x, n):
    product = float(x) * float(n)
    if product.is_integer():
        return True
    else:
        return False
