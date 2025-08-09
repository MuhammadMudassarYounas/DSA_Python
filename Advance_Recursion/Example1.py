#Example Generate Parenthesis leet Code 22
n=3 
def Generate(index,total,bracket,result,n):
    if index>=len(bracket):
        if total==0:
            result.append(" ".join(bracket))
        return
    if total > n or total<0:
        return
    bracket[index]="("
    Generate(index+1,total+1,bracket,result,n)
    bracket[index]=")"
    Generate(index+1,total-1,bracket,result,n)
    return result
print(Generate(0,0,[""]*(n*2),[],n))