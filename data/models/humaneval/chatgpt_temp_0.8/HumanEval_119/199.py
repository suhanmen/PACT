def match_parens(lst):
    stack = []
    for s in lst:
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif not stack or stack[-1] != '(':
                return 'No'
            else:
                stack.pop()
    return 'Yes' if not stack else 'No'
