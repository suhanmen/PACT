def even_odd_palindrome(n):
    # Helper function to check if a number is palindrome
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_count, odd_count = 0, 0
    for num in range(1, n+1):
        if is_palindrome(num):
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
