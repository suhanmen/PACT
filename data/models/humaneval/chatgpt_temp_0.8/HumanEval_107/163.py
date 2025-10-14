def even_odd_palindrome(n):
    # Helper function to check if a number is a palindrome
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    # Initialize counters for even and odd palindromes
    even_count = 0
    odd_count = 0

    # Check each number in the range for palindromes
    for num in range(1, n+1):
        if is_palindrome(num):
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Return the counts as a tuple
    return (even_count, odd_count)
