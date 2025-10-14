def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [num for num in lst if is_prime(num)]
    if not prime_numbers:
        return 0
    largest_prime = max(prime_numbers)
    digit_sum = sum(int(digit) for digit in str(largest_prime))
    return digit_sum
