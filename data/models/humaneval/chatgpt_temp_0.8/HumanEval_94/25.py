def skjkasdkd(lst):
    """
    You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = None
    for num in lst:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    if largest_prime is None:
        return 0
    else:
        return sum(int(digit) for digit in str(largest_prime))
