def sort_third(l: list):
    # Create a copy of the input list
    l_prime = l.copy()
    
    # Sort every third element of the list
    for i in range(2, len(l), 3):
        l_prime[i] = sorted(l[i:i+3])[0]
    
    return l_prime
