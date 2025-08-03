#example 4:Find Minimum in Rotated sorted Array LeetCode 153
num=[3,4,5,6,7,0,1,2]
def MinimumElement(nums):
    low=0
    high=len(nums)-1
    mini=float("inf")
    while low<high:
        mid =(low+high)//2
        if nums[mid]<=nums[high]:
            mini=min(mini,nums[mid])
            high=mid-1
        else:
            mini=min(mini,nums[low])
            low=mid+1
    return mini
print(MinimumElement(num))
