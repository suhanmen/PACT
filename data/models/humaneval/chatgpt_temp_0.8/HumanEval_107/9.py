def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        # Check if the number is a palindrome
        if str(i) == str(i)[::-1]:
            # If it's even, increment the even count
            if i % 2 == 0:
                even_count += 1
            # If it's odd, increment the odd count
            else:
                odd_count += 1
    
    return (even_count, odd_count)
