def simplify(x, n):
    # Convert strings to integers
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Simplify the fraction x * n
    res_num = x_num * n_num
    res_den = x_den * n_den
    gcd = abs(math.gcd(res_num, res_den))
    res_num //= gcd
    res_den //= gcd
    
    # Check if the result is a whole number
    return res_den == 1 and res_num % res_den == 0
