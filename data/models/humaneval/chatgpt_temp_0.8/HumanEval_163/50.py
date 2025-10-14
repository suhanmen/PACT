def generate_integers(a, b):
    even_digits = []
    for num in range(a, b+1):
        for digit in str(num):
            if int(digit) % 2 == 0:
                if num not in even_digits:
                    even_digits.append(num)
    return sorted(even_digits)
