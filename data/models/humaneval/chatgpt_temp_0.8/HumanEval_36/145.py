# CANNOT PARSE CODE SNIPPET
def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count
