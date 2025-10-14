def is_palindrome(n):
    return str(n) == str(n)[::-1]

def even_odd_palindrome(n):
    count_even = 0
    count_odd = 0
    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
