def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i%2==0]
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    l_prime = l.copy()
    for i in even_indices:
        l_prime[i] = even_values.pop(0)
    return l_prime
