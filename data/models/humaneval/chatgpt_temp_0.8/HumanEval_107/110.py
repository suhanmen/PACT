def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even_count = 0
    odd_count = 0
    
    for num in range(1, n+1):
        str_num = str(num)
        if str_num == str_num[::-1]:  # check if the number is a palindrome
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)
