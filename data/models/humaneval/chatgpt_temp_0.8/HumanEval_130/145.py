def tri(n):
    tribonacci = [3, 1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            tribonacci.append(1 + i / 2)
        else:
            tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])
    return tribonacci
