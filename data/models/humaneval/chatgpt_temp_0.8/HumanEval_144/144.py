def simplify(x, n):
    # Convert string representations of fractions to floats
    x = float(x.split("/")[0]) / float(x.split("/")[1])
    n = float(n.split("/")[0]) / float(n.split("/")[1])

    # Check if x * n is a whole number
    if x * n == int(x * n):
        return True
    else:
        return False
