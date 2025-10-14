"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""


import itertools

def get_total_number_of_sequences(m, n):
    def is_valid_sequence(seq):
        return all(seq[i] >= 2 * seq[i - 1] for i in range(1, len(seq)))

    def generate_sequences(m, n, current=[]):
        if len(current) == n:
            return [current] if is_valid_sequence(current) else []
        sequences = []
        start = 2 * current[-1] if current else 1
        for i in range(start, m + 1):
            sequences += generate_sequences(m, n, current + [i])
        return sequences

    return len(generate_sequences(m, n))

# Example usage
assert get_total_number_of_sequences(10, 4) == 4
