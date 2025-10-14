def sort_even(l: list):
    even_values = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    l_prime = [l[i] if i % 2 == 1 else even_values.pop(0) for i in range(len(l))]
    return l_prime
