def generate_integers(a, b):
    even_digits = []
    for num in range(a, b+1):
        num_str = str(num)
        for digit in num_str:
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))
    return sorted(even_digits)
