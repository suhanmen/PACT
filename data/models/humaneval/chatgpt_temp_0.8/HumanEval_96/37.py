def count_up_to(n):
    if n < 2:
        return []
    primes = [2]
    curr_num = 3
    while curr_num < n:
        is_prime = True
        for prime in primes:
            if curr_num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(curr_num)
        curr_num += 2
    return primes
