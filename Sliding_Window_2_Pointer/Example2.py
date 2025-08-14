#Example 2:Max Consecutive one Leet Code 1004
#brute solution
def MaxConsecutive(nums,k):
    maxi=0
    n=len(nums)
    for i in range (0,n):
        zeros=0
        for j in range(i,n):
            if nums[j]==0:
                zeros+=1
            if zeros>k:
                break
            maxi=max(maxi,j-i+1)
    return maxi
#better solution
def Max_Consecutive(nums,k):
    maxi=0
    left=0
    right=0
    zero=0
    n=len(nums)
    while right<n:
        if nums[right]==0:
            zero+=1
        while zero>k:       
            if nums[left]==0:
                zero-=1
            left+=1
        if zero<=k:
            maxi=max(maxi,right-left+1)
        right+=1
    
    return maxi
def MaxConsecutiveOnes(nums,k):
    maxi=0
    left=0
    right=0
    zero=0
    n=len(nums)
    while right<n:
        if nums[right]==0:
            zero+=1
        if zero>k: 
            if nums[left]==0:
                zero-=1      
            left+=1
        if zero<=k:
            maxi=max(maxi,right-left+1)
        right+=1
    
    return maxi


print(MaxConsecutive([1,1,1,0,0,0,1,1,1,1,0],2)) 
print(Max_Consecutive([1,1,1,0,0,0,1,1,1,1,0],2))
print(MaxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0],2))