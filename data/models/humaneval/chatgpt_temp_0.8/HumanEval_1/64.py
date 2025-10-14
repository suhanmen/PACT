from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    count = 0
    last_cut = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            if count == 0:
                result.append(paren_string[last_cut:i+1])
                last_cut = i+1
    return result
