def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """

    def tribonacci(n, memo={}):
        if n == 1:
            return 3
        if n % 2 == 0:
            return 1 + n // 2
        if n in memo:
            return memo[n]
        memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
        return memo[n]

    return [tribonacci(i) for i in range(n + 1)]