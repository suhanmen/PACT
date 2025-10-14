# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    a, b, c = 0, 0, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c
    return a
