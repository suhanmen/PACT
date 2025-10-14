def generate_integers(a, b):
    even_digits = []
    for n in range(a, b+1):
        digits = [int(d) for d in str(n)]
        for d in digits:
            if d % 2 == 0:
                even_digits.append(n)
                break
    return sorted(even_digits)
