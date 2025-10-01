def eval_rpn(tokens):
    """
    Evaluate a list of tokens in Reverse Polish Notation.

    :param tokens: List of strings, e.g., ["2","1","+","3","*"]
    :return: integer result of evaluation
    """
    stack = []
    operators = {"+", "-", "*", "/"}  # Supported operators

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Integer division that truncates toward zero
                stack.append(int(a / b))
        else:
            # token is a number
            stack.append(int(token))

    return stack[0]
