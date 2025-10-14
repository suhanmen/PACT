# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    # Define the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the variables for the three most recent fibfib numbers
    a, b, c = 0, 1, 1
    
    # Compute the n-th fibfib number
    for i in range(3, n+1):
        d = a + b + c
        a, b, c = b, c, d
        
    return c
