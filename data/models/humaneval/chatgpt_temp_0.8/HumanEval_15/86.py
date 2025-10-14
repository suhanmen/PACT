def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    sequence = "0"
    for i in range(1, n+1):
        sequence += " " + str(i)
    return sequence
