class solution:
    def PrefixToInfix(self,s):
        n=len(s)
        stack=[]
        for char in range(n-1,-1,-1):#s[::-1]
            if s[char].isalnum():
                stack.append(s[char])
            else:
                operand2=stack.pop()
                operand1=stack.pop()

                new_expe=f"({operand2}{s[char]}{operand1})"

                stack.append(new_expe)

        return stack[-1]
PTI=solution()
print(PTI.PrefixToInfix("*+PQ-MN"))