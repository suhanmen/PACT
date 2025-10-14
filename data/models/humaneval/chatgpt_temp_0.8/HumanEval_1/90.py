from collections import deque
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    q = deque()
    for c in paren_string.replace(' ', ''):
        if c == '(':
            q.append(c)
        elif c == ')':
            q.pop()
            if not q:
                groups.append(''.join(q))
    return groups
