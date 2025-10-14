def get_odd_collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    odd_sequence = [x for x in sequence if x % 2 == 1]
    return sorted(odd_sequence)
