def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        stack = []
        depth = 0
        for c in group:
            if c == '(':
                stack.append(c)
                depth = max(depth, len(stack))
            elif c == ')':
                stack.pop()
        depths.append(depth)
    return depths
