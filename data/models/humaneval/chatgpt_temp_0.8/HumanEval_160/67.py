def do_algebra(operator, operand):
    """
    Given two lists operator and operand, build an algebraic expression using the operators and
    operands and return the evaluation of this expression.

    Args:
        operator (list): A list of basic algebra operations. Can include +, -, *, //, and **.
        operand (list): A list of non-negative integers to be used in the expression.

    Returns:
        int: The result of the algebraic expression.

    Example:
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        result = 2 + 3 * 4 - 5
        => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    result = operand[0]  # start with the first operand

    for i in range(len(operator)):
        op = operator[i]
        num = operand[i+1]

        if op == '+':
            result += num
  
