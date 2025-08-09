def AllBinaryString(N):
    Result=[]
    def Backtrack(index,flag,Number):
        if index>=N:
            Result.append(" ".join(Number))
            return
        Number[index]="0"
        Backtrack(index+1,True,Number)
        if flag==True:
            Number[index]="1"
            Backtrack(index+1,False,Number)
            Number[index]="0"
    Backtrack(0,True,["0"]*N)
    return Result
print(AllBinaryString(3))