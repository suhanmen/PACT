"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""



def newman_conway(n):
    if n == 1 or n == 2:
        return 1
    sequence = [0, 1, 1]
    for i in range(3, n + 1):
        sequence.append(sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]])
    return sequence[n]


def sequence(n):
    return newman_conway(n)

assert sequence(10) == 6
