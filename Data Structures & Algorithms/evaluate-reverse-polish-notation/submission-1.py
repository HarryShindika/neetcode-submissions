class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(l,r,op):
            if op == '+':
                return l + r
            elif op == '-':
                return l - r
            elif op == '*':
                return l * r
            else:
                return int(l / r)

        stack = []

        ops = {'+','-','*','/'}

        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                r = stack.pop()
                l = stack.pop()
                stack.append(calc(l,r,i))

        return stack[0]


        
        