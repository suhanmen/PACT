"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""



def is_samepatterns(colors, patterns):
    if not colors or not patterns or len(colors) != len(patterns):
        return False

    pattern_dict = {}
    used_patterns = set()

    for color, pattern in zip(colors, patterns):
        if color in pattern_dict:
            if pattern_dict[color] != pattern:
                return False
        else:
            if pattern in used_patterns:
                return False
            pattern_dict[color] = pattern
            used_patterns.add(pattern)

    return True

# Example usage:
# assert is_samepatterns(["red","green","green"], ["a", "b", "b"]) == True
