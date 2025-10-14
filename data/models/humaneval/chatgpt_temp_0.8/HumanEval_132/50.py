def is_nested(string):
    stack = [] # create an empty stack to keep track of opening brackets
    nested = False # initialize nested to False
    
    for bracket in string:
        if bracket == '[':
            stack.append(bracket) # add opening brackets to the stack
        elif bracket == ']':
            if stack: # check if there is an opening bracket to match with the closing bracket
                stack.pop() # remove the last opening bracket from the stack
                nested = True # set nested to True since there is at least one nested bracket
            else:
                continue # ignore the closing bracket if there is no matching opening bracket
    
    if nested and stack: # if there is at least one nested bracket and there are unmatched opening brackets
        return True
    else:
        return False
