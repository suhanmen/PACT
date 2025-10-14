def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even_count = 0
    odd_count = 0

    # Iterate over the range of numbers from 1 to n
    for num in range(1, n + 1):
        # Check if the number is a palindrome
        if str(num) == str(num)[::-1]:
            # If the number is even, increment the even_count variable
            if num % 2 == 0:
                even_count += 1
            # If the number is odd, increment the odd_count variable
            else:
                odd_count += 1

    # Return a tuple with the even and odd counts
    return (even_count, odd_count)
