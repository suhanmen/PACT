import re

def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None

assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)