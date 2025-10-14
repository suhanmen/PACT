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

    # Helper function to check if a number is palindrome or not
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    # Initialize variables to count even and odd palindromes
    even_count = 0
    odd_count = 0

    # Loop through the range from 1 to n (inclusive)
    for i in range(1, n+1):
        # Check if the number is palindrome or not
        if is_palindrome(i):
            # Increment the corresponding count variable
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Return the tuple of even and odd palindrome counts
    return (even_count, odd_count)
