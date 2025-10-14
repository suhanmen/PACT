def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list should be one less than the operand list")

    # Evaluate the expression using the provided operators and operands
    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError("Invalid operator: {}".format(op))

    return result
