def generate_integers(a, b):
    result = []
    for num in range(a, b+1):
        for digit in str(num):
            if int(digit) % 2 == 0:
                result.append(int(digit))
    return sorted(list(set(result)))
