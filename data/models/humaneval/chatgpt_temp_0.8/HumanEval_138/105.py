def is_equal_to_sum_even(n):
    count = 0
    for i in range(2, n):
        if i % 2 == 0 and n - i >= 2 and (n - i) % 2 == 0:
            count += 1
    return count == 2
