class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        first = 0
        second = 0
        stack = []

        for s in tokens:
            if s not in '+-*/':
                stack.append(int(s))
            else:
                second = stack.pop()
                first = stack.pop()

                if s == '+':
                    stack.append(first + second)
                elif s == '-':
                    stack.append(first - second)
                elif s == '*':
                    stack.append(first * second)
                elif s == '/':
                    stack.append(int(first / second))
        return stack[0]

        