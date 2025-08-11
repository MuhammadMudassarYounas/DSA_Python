class Infix_To_Postfix:
    def Priority(self,ch):
        if ch=="+" or ch=="-":
            return 1
        if ch=="*" or ch=="/":
            return 2
        if ch=="^":
            return 3
        return 0
    def InfixToPostfix(self,s):
        s=s[::-1]
        s=s.replace("(","temp").replace(")","(").replace("temp",")")
        print(s)
        Stack=[]
        Result=[]
        for char in s:
            if ("a"<=char <="z") or ("A"<=char<="Z")or("0"<=char<="9"):
                Result.append(char)
            elif char=="(":
                Stack.append(char)
            elif char==")":
                while Stack and Stack[-1]!="(":
                    Result.append(Stack.pop())
                Stack.pop()
            else:
                while Stack and self.Priority(Stack[-1])>=self.Priority(char):
                    Result.append(Stack.pop())
                Stack.append(char)
        while Stack:
                Result.append(Stack.pop())

        return ("".join(Result[::-1]))

ITP=Infix_To_Postfix()

print(ITP.InfixToPostfix("a+b*(c^d-e)"))
