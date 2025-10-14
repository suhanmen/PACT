def solve(N):
    binary_sum = 0
    while N > 0:
        binary_sum += N % 2
        N //= 2
    return bin(binary_sum)[2:]
