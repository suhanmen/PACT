def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for divisor in range(n-1, 0, -1):
        if n % divisor == 0:
            return divisor
    return None
