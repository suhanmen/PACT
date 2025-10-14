python
def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        depth = 0
        max_depth = 0
        for c in group:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
        depths.append(max_depth)
    return depths
