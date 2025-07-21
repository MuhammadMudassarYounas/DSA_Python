#Example 1: Merge two sorted array without duplicate 
n1 =[1,2,2,3,4,4,5,6,7,7,7,8,10,10,11,12,15,17,]
n2=[1,1,2,3,3,4,5,5,6,6,7,9,10]
def merge(num1,num2):
    result=[]
    i,j=0,0
    n,m=len(num1),len(num2)
    while i<n and j<m:
        if (num1[i]<num2[j]):
            if(num1[i] not in result):
                result.append(num1[i])
            i+=1
        else:
            if(num2[j] not in result):
                result.append(num2[j])
            j+=1
    if(i<n):
        while i<n:
            if(num1[i] not in result):
                result.append(num1[i])
            i+=1
    if(j<m):
        while j<m:
            if(num2[j] not in result):
                result.append(num2[j])
            j+=1
    return result
print(merge(n1,n2))