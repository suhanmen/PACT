# CANNOT PARSE CODE SNIPPET
python
def is_prime(num: int) -> bool:
    """
    is_prime checks whether a number is prime or not.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n should be a positive integer")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        prev1 = 2
        prev2 = 3
        count = 2
        while count < n:
            curr = prev1 + prev2
            if is_prime(curr):
                count += 1
                if count == n:
                    return curr
            prev1 = prev2
            prev2 = curr
        raise ValueError("Cannot find a Fibonacci prime for the given n")
