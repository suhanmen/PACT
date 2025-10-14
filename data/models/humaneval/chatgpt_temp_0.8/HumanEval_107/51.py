def even_odd_palindrome(n):
    # utility function to check if a number is palindrome
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    # initialize counters for even and odd palindromes
    even_count = 0
    odd_count = 0

    # iterate over the range of numbers from 1 to n
    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # return the tuple with the counts
    return (even_count, odd_count)
