def generate_integers(a, b):
    result = []
    for x in range(min(a, b), max(a, b)+1):
        for digit in str(x):
            if int(digit) % 2 == 0:
                result.append(int(digit))
    return sorted(list(set(result)))
