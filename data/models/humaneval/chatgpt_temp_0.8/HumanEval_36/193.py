def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(1, n):
        if (i % 11 == 0 or i % 13 == 0) and '7' in str(i):
            count += str(i).count('7')
    return count
