def check_parenthesis(expression : str) -> bool: # type hint
    stack = []
    for c in expression:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False

            else:
                stack.pop()

    return len(stack) == 0

print(check_parenthesis("()(")) # len(stack) == 1 즉 False
print(check_parenthesis("()")) # len(stack) == 0 즉 True
print(check_parenthesis("))()")) # 처음 입력받는게 닫힌 괄호라서 바로 False
print(check_parenthesis("(()()()()()()())"))