# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    # Define the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Define the recursive formula
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
