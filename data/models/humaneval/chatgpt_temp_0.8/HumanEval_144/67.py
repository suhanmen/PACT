def simplify(x, n):
    # Convert fractions to integers
    x_num, x_den = map(int, x.split("/"))
    n_num, n_den = map(int, n.split("/"))

    # Simplify fractions
    gcd_x = math.gcd(x_num, x_den)
    gcd_n = math.gcd(n_num, n_den)

    x_num //= gcd_x
    x_den //= gcd_x
    n_num //= gcd_n
    n_den //= gcd_n

    # Check if x * n is a whole number
    if (x_num * n_num) % (x_den * n_den) == 0:
        return True
    else:
        return False
