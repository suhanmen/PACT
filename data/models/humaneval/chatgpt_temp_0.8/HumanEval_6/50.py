def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        max_level = 0
        depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_level = max(max_level, depth)
            elif char == ')':
                depth -= 1
        levels.append(max_level)
    return levels
