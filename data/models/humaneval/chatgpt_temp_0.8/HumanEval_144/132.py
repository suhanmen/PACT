python
def simplify(x, n):
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    # Calculate the product of the numerators and denominators
    product_num = int(x_num) * int(n_num)
    product_den = int(x_den) * int(n_den)
    # Check if the product is a whole number
    return product_num % product_den == 0
