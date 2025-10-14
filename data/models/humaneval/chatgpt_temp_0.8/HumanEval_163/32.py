def generate_integers(a, b):
    result = []
    for i in range(a, b+1):
        digits = [int(d) for d in str(i) if int(d) % 2 == 0]
        if digits and all(d <= i for d in digits):
            result.extend(digits)
    return sorted(result)
