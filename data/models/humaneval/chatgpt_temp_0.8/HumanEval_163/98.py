def generate_integers(a, b):
    even_digits = []
    start = min(a,b)
    end = max(a,b)
    for num in range(start, end+1):
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))
    return sorted(list(set(even_digits)))
