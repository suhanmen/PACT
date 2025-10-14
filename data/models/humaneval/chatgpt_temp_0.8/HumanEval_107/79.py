def is_palindrome(num):
    # function to check if a number is palindrome or not
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    # function to count even and odd palindromes in range(1, n)
    even_count = 0
    odd_count = 0
    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
