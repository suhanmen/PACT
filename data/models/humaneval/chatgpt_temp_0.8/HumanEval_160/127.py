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
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list is not equal to the length of operand list minus one.")
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand is not a list of non-negative integers.")
    if not operator:
        raise ValueError("Operator list is empty.")
    if len(operand) < 2:
        raise ValueError("Operand list has less than two operands.")

    expression = str(operand[0])
    for i in range(1, len(operand)):
        expression += ' ' + operator[i-1] + ' ' + str(operand[i])

    return eval(expression)
