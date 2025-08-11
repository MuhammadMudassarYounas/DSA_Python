class solution:
    def PostfixToInfix(self,s):
        print(len(s))
        stack=[]
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                operand2=stack.pop()
                operand1=stack.pop()

                new_expe=f"{char}{operand1}{operand2}"

                stack.append(new_expe)

        return stack[-1]
PTI=solution()
print(PTI.PostfixToInfix("AB-DE*/"))