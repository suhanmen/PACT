def generate_integers(a, b):
    even_digits = []
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        digits = [int(d) for d in str(i)]
        for digit in digits:
            if digit % 2 == 0:
                even_digits.append(i)
                break
    return even_digits
