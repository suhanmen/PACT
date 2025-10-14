def generate_integers(a, b):
    result = []
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        digits = [int(d) for d in str(i) if int(d) % 2 == 0]
        result += digits
    return sorted(list(set(result)))
