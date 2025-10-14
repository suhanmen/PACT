def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    count = 0
    start = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count == 0:
            result.append(paren_string[start:i+1])
            start = i+1
    return result
