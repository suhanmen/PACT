def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [3]
    else:
        seq = [0, 0, 3] # initialize the sequence with the first three numbers
        for i in range(3, n+1):
            if i % 2 == 0:
                seq.append(1 + i // 2) # append the next even number
            else:
                next_num = seq[-1] + seq[-2] + seq[-3] # calculate the next odd number
                seq.append(next_num)
        return seq
