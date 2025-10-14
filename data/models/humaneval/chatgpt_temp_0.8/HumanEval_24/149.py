def largest_divisor(n: int) -> int:
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            largest = i
    return largest
