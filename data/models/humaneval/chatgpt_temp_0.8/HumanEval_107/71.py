def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even_count = 0
    odd_count = 0
    
    # Check each number in the range for palindromic property
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:  # Check if the palindrome is even
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)
