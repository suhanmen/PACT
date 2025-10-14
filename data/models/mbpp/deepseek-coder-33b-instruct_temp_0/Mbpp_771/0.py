Here is the Python function to check if the given expression is balanced or not:

```python
def check_expression(expr):
    stack = []
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))

    for i in expr:
        if i in open_tup:
            stack.append(map[i])
        elif i in close_tup:
            if not stack or i != stack.pop():
                return False
    if stack:
        return False
    return True

# Test the function
print(check_expression("{()}[{}]"))  # Output: True
```

This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the top of the stack is the corresponding opening bracket. If it is, it pops the opening bracket from the stack. If it is not, or if the stack is empty, it returns False. If it successfully goes through the entire expression and the stack is empty, it returns True.
