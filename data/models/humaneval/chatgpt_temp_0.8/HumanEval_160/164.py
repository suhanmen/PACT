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
    
    # Create an empty string to hold the algebraic expression
    expression = ''
    
    # Loop through the length of the operator list
    for i in range(len(operator)):
        
        # Add the current operand to the expression
        expression += str(operand[i])
        
        # Add the current operator to the expression
        expression += operator[i]
    
    # Add the last operand to the expression
    expression += str(operand[-1])
    
    # Evaluate the expression and return the result
    return eval(expression)
