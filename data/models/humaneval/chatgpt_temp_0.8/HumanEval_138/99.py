def is_equal_to_sum_even(n):
    count = 0
    for i in range(2, n//2 + 1, 2):
        for j in range(i, n//2 + 1, 2):
            for k in range(j, n//2 + 1, 2):
                if i + j + k == n:
                    count += 1
    return count == 1
