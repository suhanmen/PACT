def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """

    # count the number of opening and closing brackets
    num_opening_brackets = brackets.count("<")
    num_closing_brackets = brackets.count(">")
    
    # if the counts don't match, then there is an unclosed bracket
    if num_opening_brackets != num_closing_brackets:
        return False
    
    # loop through each bracket in the string
    stack = []
    for bracket in brackets:
        if bracket == "<":
            # if it's an opening bracket, add it to the stack
            stack.append(bracket)
        elif bracket == ">":
            # if it's a closing bracket, check if there is a matching opening bracket in the stack
            if len(stack) == 0:
                # if there is no matching opening bracket, then the bracketing is incorrect
                return False
            else:
                # if there is a matching opening bracket, remove it from the stack
                stack.pop()
    
    # if we've reached the end of the loop and the stack is empty, the
