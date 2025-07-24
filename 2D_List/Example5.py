#Example 5:4Sum Problem LeetCode 18
#brute solution
Arr=[-1,0,-1,0,-2,2,]
def Sum(Arr):
    Result=set()
    n=len(Arr)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if Arr[i]+Arr[j]+Arr[k]+Arr[l]==0:
                        temp=[Arr[i],Arr[j],Arr[k],Arr[l]]
                        temp.sort()
                        Result.add(tuple(temp))
    return [list(ans) for ans in Result]
print(Sum(Arr))
#optimal Solution
num=[1,2,1,3,1,1,2,3,3,4,5,4,5,4]
def FourSum(nums,target):
    Result=[]
    nums.sort()
    n=len(nums)
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=n-1
            while k<l:
                total=nums[i]+nums[j]+nums[k]+nums[l]
                if total != target:
                    k+=1
                    l-=1
                else:
                    Result.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
    return Result
print(FourSum(num,8))

