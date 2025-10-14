def fizz_buzz(n: int):
    count = 0
    for num in range(n):
        if (num % 11 == 0 or num % 13 == 0) and '7' in str(num):
            count += 1
    return count
