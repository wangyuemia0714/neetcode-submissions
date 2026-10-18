class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
# I can use a stack to stock numbers, and pop first and seccond number when meet the operators.
        stack = [] 
        # create an empty stack 
        for token in tokens: 
            # iterate the list
            if token not in '+-*/':
                stack.append(int(token))
                # push the number in stack
            
            else:
                first = int(stack.pop())
                second = int(stack.pop()) 
                # pop the first and second number when meet an operator
                if token == '+':
                    result = second + first
                elif token == '-':
                    result = second - first
                elif token == '*':
                    result = second * first
                elif token == '/':
                    result = abs(second) // abs(first) 
# use the absolute value here, because in python, "//" means floor devision, this doesn't work if the result is a negtive one, because "Assume that division between integers always truncates toward zero." 
                    if (second<0) != (first<0):
                        result = -result
                stack.append(result)
        return stack.pop()


            




        