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
    # Check that the operator list has at least one operator, and operand list has at least two operands.
    if len(operator) < 1 or len(operand) < 2:
        return None
    
    # Initialize the result to be the first operand.
    result = operand[0]
    
    # Loop through the operator list and apply each operator to the result and the next operand.
    for i in range(len(operator)):
        op = operator[i]
        next_operand = operand[i+1]
        if op == '+':
            result += next_operand
        elif op == '-':
            result -= next_operand
        elif op == '*':
            result *= next_operand
        elif op == '//':
            result //= next_operand
        elif op == '**':
            result **= next_operand
    
    return result
