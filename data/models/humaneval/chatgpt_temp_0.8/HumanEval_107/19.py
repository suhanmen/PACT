def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    # Define a function to check if a number is a palindrome
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    # Initialize counters for even and odd palindromes
    even_count = 0
    odd_count = 0

    # Loop through numbers from 1 to n
    for i in range(1, n+1):
        # Check if number is a palindrome
        if is_palindrome(i):
            # Increment even/odd palindrome counter based on parity
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Return tuple of even and odd palindrome counts
    return (even_count, odd_count)
