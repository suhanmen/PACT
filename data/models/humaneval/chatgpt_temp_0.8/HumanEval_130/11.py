python
def tri(n):
    tribonacci_seq = [3] # the first number in the Tribonacci sequence is 3
    if n == 0:
        return tribonacci_seq
    elif n == 1:
        tribonacci_seq.append(1 + (n / 2))
        return tribonacci_seq
    elif n >= 2:
        tribonacci_seq.append(1 + (n / 2))
        for i in range(2, n+1):
            if i % 2 == 0:
                tribonacci_seq.append(1 + (i / 2))
            else:
                tribonacci_seq.append(tribonacci_seq[i-1] + tribonacci_seq[i-2] + tribonacci_seq[i+1])
        return tribonacci_seq
