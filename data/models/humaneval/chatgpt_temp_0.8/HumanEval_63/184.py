def fibfib(n: int):
    fibfib0 = 0
    fibfib1 = 0
    fibfib2 = 1
    
    for i in range(3, n+1):
        fibfib3 = fibfib0 + fibfib1 + fibfib2
        fibfib0 = fibfib1
        fibfib1 = fibfib2
        fibfib2 = fibfib3
    
    if n == 0 or n == 1:
        return 0
    else:
        return fibfib2
