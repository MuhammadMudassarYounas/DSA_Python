#Explain binary search
num=[2,4,6,7,9,11,13,15,18]
def Binary(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid =(low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] <target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(Binary(num,13))
#using Recursion in binary search
n=len(num)
def binary(nums,low,high,target):
    if low>high:
        return -1
    mid =(low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] <target:
       return binary(nums,mid+1,high,target)
    else:
       return binary(nums,low,mid-1,target)
    
print(binary(num,0,n-1,13))
    