def even_odd_palindrome(n):
    evens = 0
    odds = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                evens += 1
            else:
                odds += 1
    return (evens, odds)
