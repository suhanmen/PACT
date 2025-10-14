def generate_integers(a, b):
    even_digits = []
    for num in range(a, b+1):
        num_str = str(num)
        for digit in num_str:
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))
    even_digits.sort()
    return even_digits
