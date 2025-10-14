def tri(n):
    seq = [3] # initialize sequence with first element
    if n > 0:
        seq.append(1) # add second element if n > 0
    if n > 1:
        seq.append(2) # add third element if n > 1
    
    for i in range(3, n+1): # loop to generate subsequent elements up to n
        if i % 2 == 0:
            seq.append(1 + i // 2) # calculate even terms
        else:
            seq.append(seq[-1] + seq[-2] + seq[-3]) # calculate odd terms
    
    return seq
