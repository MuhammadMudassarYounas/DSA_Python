#Example 8:Minimum Number PlatForms Required geek for geek
#brute solution
Arr=[900,940,950,1100,1500,1800]
Dep=[910,1200,1120,1130,1900,2000]
def Minimum(Arr,Dep):
    ans=1
    for i in range(0,len(Arr)):
        count=1
        for j in range(i+1,len(Arr)):
            if (Arr[i]>=Arr[j] and Arr[i]<=Dep[j]) or (Arr[j]>=Arr[i] and Arr[j]<=Dep[i]):
                count+=1
            ans=max(ans,count)
        return ans
print(Minimum(Arr,Dep))
def Minimum_Platforms(Arr,Dep):
    Arr.sort()
    Dep.sort()
    ans=1
    count=1
    i=1
    j=0
    while i<len(Arr) and j<len(Dep):
        if Arr[i]<=Dep[j]:
            count+=1
            i+=1
        else:
            count-=1
            j+=1
        ans=max(ans,count)
    return ans
print(Minimum_Platforms(Arr,Dep))