def is_balanced(expression):
    brackets = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in expression:
        if c in '([{':
            brackets.append(c)
        elif c in ')]}':
            if not brackets:
                return False
            top = brackets.pop()
            if top != pairs[c]:
                return False

    return len(brackets) == 0


expr1 = "{a, (b, [c, d])}"
expr2 = "{a, (b, [c, d)])}"

print(f"{expr1} is balanced:", is_balanced(expr1))
print(f"{expr2} is balanced:", is_balanced(expr2))