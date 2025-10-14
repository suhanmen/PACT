def do_algebra(operator, operand):
    # Build the algebraic expression from the operator and operand lists
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i+1])

    # Evaluate the algebraic expression and return the result
    return eval(expression)
