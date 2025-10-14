def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:  # checking if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
