def generate_integers(a, b):
    even_digits = []
    for n in range(a, b+1):
        for digit in str(n):
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))
    return sorted(even_digits)
