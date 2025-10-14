def generate_integers(a, b):
    even_digits = []
    for i in range(a, b+1):
        for j in str(i):
            if int(j) % 2 == 0:
                even_digits.append(int(j))
    return sorted(set(even_digits))
