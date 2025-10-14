def is_palindrome(number):
    """
    Given a number, return True if it's a palindrome, False otherwise.
    """
    return str(number) == str(number)[::-1]

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)
