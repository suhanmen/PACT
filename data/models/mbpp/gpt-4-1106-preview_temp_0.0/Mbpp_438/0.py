"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""



def count_bidirectional(pairs):
    count = 0
    seen = set()
    for a, b in pairs:
        if (a, b) not in seen and (b, a) not in seen:
            seen.add((a, b))
        elif (b, a) in seen:
            count += 1
    return count

assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
