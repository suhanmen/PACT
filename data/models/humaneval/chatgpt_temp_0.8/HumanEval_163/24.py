def generate_integers(a, b):
    even_digits = []
    for n in range(a, b+1):
        for digit in str(n):
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))
    return sorted(set(even_digits))
