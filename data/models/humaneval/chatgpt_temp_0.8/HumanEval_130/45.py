def tri(n):
    tribonacci = [3]
    if n == 0:
        return tribonacci
    tribonacci.append(1 + n // 2)  # add second element
    if n == 1:
        return tribonacci
    for i in range(2, n + 1):
        if i % 2 == 0:
            tribonacci.append(1 + i // 2)  # formula for even n
        else:
            tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i+1])  # formula for odd n
    return tribonacci
