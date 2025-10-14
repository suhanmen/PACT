def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    if len(operator) + 1 != len(operand):
        return "Invalid input: length of operator list should be one less than length of operand list"
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        return "Invalid input: operand list should only contain non-negative integers"
    if not all(op in ['+', '-', '*', '//', '**'] for op in operator):
        return "Invalid input: operator list should only contain basic algebra operations"

    expression = str(operand[0])
    for i in range(len(operator)):
        expression += " " + operator[i] + " " + str(operand[i+1])
    return eval(expression)
