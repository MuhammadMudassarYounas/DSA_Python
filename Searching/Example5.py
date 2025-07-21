#Example 5:Maximum SubArray Sum
# brute solution
nums=[-2,1,-3,4,-1,2,1,-5,4]

def SubArray(nums):
    total=0
    maxi=float("-inf")
    for i in range(0,len(nums)):
        total=0
        for j in range(i,len(nums)):
            total=total+nums[j]
            if total>maxi:
                maxi=total
    return maxi
print(SubArray(nums))
#optimal solution
def SubArraySum(nums):
    total=0
    maximum=float("-inf")
    for i in range(0,len(nums)):
        total=total+nums[i]
        if total>maximum:
            maximum=total
        if (total<0):
            total=0  
    return maximum
print(SubArraySum(nums))

