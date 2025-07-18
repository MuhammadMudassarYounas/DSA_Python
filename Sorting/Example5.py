#Example 5: Move Zero element from right side 
#Better solution
num =[1,0,1,2,4,8,9,0,11,0]
def MoveZero(num):
    Result=[]
    for i in range(0,len(num)):
        if num[i]!=0:
            Result.append(num[i])
    for i in range(0,len(Result)):
        num[i]=Result[i]
    for i in range(len(Result),len(num)):
        num[i]=0
    print(num)
MoveZero(num)

#Optimal Solution
def MoveZeroToRight(num):
    if len(num)==0:
        return
    i=0
    while i<len(num):
        if i==0:
            break
        i+=1
    if i==len(num):
        return
    j=i+1
    while j<len(num):
        if num[j]!=0:
            num[i],num[j]=num[j],num[i]
            i+=1
        j+=1
    print(num)
MoveZeroToRight(num)
    

