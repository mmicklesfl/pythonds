def valid_parentheses(parens):
    """Are the parentheses validly balanced?

    >>> valid_parentheses("()")
    True

    >>> valid_parentheses("()()")
    True

    >>> valid_parentheses("(()())")
    True

    >>> valid_parentheses(")()")
    False

    >>> valid_parentheses("())")
    False

    >>> valid_parentheses("((())")
    False

    >>> valid_parentheses(")()(")
    False
    """
    stack = []
    opening_parentheses = set("([{")
    closing_parentheses = set(")]}")
    parentheses_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for paren in parens:
        if paren in opening_parentheses:
            stack.append(paren)
        elif paren in closing_parentheses:
            if not stack or stack[-1] != parentheses_map[paren]:
                return False
            stack.pop()
    return len(stack) == 0
