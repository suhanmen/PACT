def simplify(x, n):
    # Convert x and n to floats
    x = float(x.split("/")[0]) / float(x.split("/")[1])
    n = float(n.split("/")[0]) / float(n.split("/")[1])
    
    # Check if x * n is a whole number
    return x * n == int(x * n)
