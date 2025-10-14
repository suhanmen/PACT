def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            for digit in str(i):
                if digit == '7':
                    count += 1
    return count
