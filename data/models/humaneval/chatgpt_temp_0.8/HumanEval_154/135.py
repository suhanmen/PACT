# CANNOT PARSE CODE SNIPPET
def cycpattern_check(a, b):
    # Concatenate the first word with itself to handle rotations
    a += a
    # Check if the second word or any of its rotations is a substring in the first word
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            return True
    return False
