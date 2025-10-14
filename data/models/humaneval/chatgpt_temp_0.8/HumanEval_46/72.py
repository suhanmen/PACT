def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    fibs = [0, 0, 2, 0]
    for i in range(3, n+1):
        fibs[i%4] = fibs[(i-1)%4] + fibs[(i-2)%4] + fibs[(i-3)%4] + fibs[(i-4)%4]
    
    return fibs[n%4]
