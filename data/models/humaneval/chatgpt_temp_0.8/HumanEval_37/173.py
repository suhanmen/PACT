def sort_even(l: list):
    even_indices = [i for i in range(0, len(l), 2)]
    even_values = [l[i] for i in even_indices]
    sorted_even_values = sorted(even_values)
    l_prime = l.copy()
    for i in range(len(sorted_even_values)):
        l_prime[even_indices[i]] = sorted_even_values[i]
    return l_prime
