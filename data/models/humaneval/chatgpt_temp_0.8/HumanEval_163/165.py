def generate_integers(a, b):
    even_digits = []
    for number in range(a, b+1):
        digits = [int(digit) for digit in str(number)]
        for digit in digits:
            if digit % 2 == 0 and digit not in even_digits:
                even_digits.append(digit)
    even_digits.sort()
    return even_digits
