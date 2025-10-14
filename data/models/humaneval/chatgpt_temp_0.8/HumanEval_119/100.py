def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    # combine the two strings into one string
    combined_string = lst[0] + lst[1]

    # use a stack to keep track of the opening parentheses
    stack = []

    # iterate through the characters in the combined string
    for char in combined_string:

        # if the character is an opening parenthesis, add it to the stack
        if char == "(":
            stack.append(char)

        # if the character is a closing parenthesis, check if the stack is empty
        elif char == ")":
            if len(stack) == 0:
                return "No"
            else:
                stack.pop()

    # if the stack is empty, all parentheses have been matched and the string is good
    if len(stack) == 0:
        return "Yes"
    else:
        return "No"
