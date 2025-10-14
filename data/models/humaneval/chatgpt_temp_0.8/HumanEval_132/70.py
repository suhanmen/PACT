def is_nested(string):
    opening_brackets = []
    for bracket in string:
        if bracket == "[":
            opening_brackets.append(bracket)
        elif bracket == "]":
            if opening_brackets:
                opening_brackets.pop()
            else:
                return False
            if not opening_brackets:
                return True
    return False
