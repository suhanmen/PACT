def is_equal_to_sum_even(n):
    count = 0
    for i in range(2, n):
        if i % 2 == 0:
            for j in range(i, n):
                if j % 2 == 0:
                    for k in range(j, n):
                        if k % 2 == 0:
                            for l in range(k, n):
                                if l % 2 == 0 and i + j + k + l == n:
                                    count += 1
 
    return count == 1
