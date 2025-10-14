def sort_even(l: list):
    even_sorted = sorted([l[i] for i in range(0, len(l), 2)])
    l_prime = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_prime.append(l[i])
        else:
            l_prime.append(even_sorted.pop(0))
    return l_prime
