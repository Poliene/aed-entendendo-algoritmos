from src.my_stack import MyStack

def is_valid_parentheses(s):
    stack = MyStack()

    for char in s:
        if char in "([{":
            stack.push(char)
        else:
            if stack.is_empty():
                return False

            topo = stack.pop()

            if char == ")" and topo != "(":
                return False
            if char == "]" and topo != "[":
                return False
            if char == "}" and topo != "{":
                return False

    return stack.is_empty()