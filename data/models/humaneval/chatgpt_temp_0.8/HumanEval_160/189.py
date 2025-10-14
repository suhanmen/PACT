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
    assert len(operator) == len(operand) - 1, "Operator list length doesn't match operand list length"
    assert len(operand) >= 2, "Operand list should have at least two values"
    assert all(isinstance(i, int) and i >= 0 for i in operand), "Operand list should only contain non-negative integers"

    # Build the algebraic expression string
    expression = str(operand[0])
    for i in range(1, len(operand)):
        expression += ' ' + operator[i-1] + ' ' + str(operand[i])

    # Evaluate the expression and return the result
    return eval(expression)
